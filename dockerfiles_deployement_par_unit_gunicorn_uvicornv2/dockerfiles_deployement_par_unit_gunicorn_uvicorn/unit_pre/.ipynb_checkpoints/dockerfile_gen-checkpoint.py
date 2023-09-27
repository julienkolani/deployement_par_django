import os

# Obtenir la liste des fichiers du répertoire courant
current_directory = os.getcwd()
project_files = [f for f in os.listdir(current_directory) if os.path.isdir(f)]

# Afficher la liste des projets disponibles
print("Projets disponibles dans le répertoire courant:")
for i, project in enumerate(project_files, start=1):
    print(f"{i}. {project}")

# Demander à l'utilisateur de choisir un projet
while True:
    try:
        choice = int(input("Choisissez un numéro de projet (1, 2, ...) : "))
        if 1 <= choice <= len(project_files):
            django_project_name = project_files[choice - 1]
            break
        else:
            print("Choix invalide. Veuillez choisir un numéro valide.")
    except ValueError:
        print("Veuillez entrer un numéro valide.")
        
# Variables
workdir = "/home/app"
python_version = "3.9.18-slim-bullseye"

# Étape 1 : Construction de l'environnement virtuel et installation des dépendances Django
dockerfile_content = f"""
# Étape 1 : Construction de l'environnement virtuel et installation des dépendances Django
FROM debian:stable-slim AS builder

RUN mkdir -p {workdir}

# Installation des outils nécessaires
RUN rm -f /etc/apt/apt.conf.d/docker-clean; echo 'Binary::apt::APT::Keep-Downloaded-Packages "true";' > /etc/apt/apt.conf.d/keep-cache

RUN --mount=type=cache,target=/var/cache/apt,sharing=locked \
    --mount=type=cache,target=/var/lib/apt,sharing=locked \
    apt-get update -y \
    && apt-get -o APT::Install-Recommends=false upgrade -y \
    && apt-get install -y \
    python3 \
    python3-venv \
    python3-pip ; \
    apt-get autoremove -y

# Création de l'environnement virtuel
RUN python3 -m venv {workdir}/my_app_venv

# Copie des fichiers du projet Django dans le conteneur
COPY {django_project_name}/requirements.txt {workdir}/requirements.txt

# Installation des dépendances Django dans l'environnement virtuel
RUN --mount=type=cache,target=/root/.cache \
    {workdir}/my_app_venv/bin/pip install -r {workdir}/requirements.txt \
    && {workdir}/my_app_venv/bin/pip install uvicorn

# Étape 2 : Création du conteneur final
FROM debian:stable-slim

# Copier l'environnement virtuel depuis l'étape précédente
COPY --from=builder {workdir}/my_app_venv {workdir}/my_app_venv

# Définir les variables d'environnement
ENV PATH="{workdir}/my_app_venv/bin:$PATH"

RUN mkdir -p {workdir}/{django_project_name}

COPY {django_project_name} {workdir}/{django_project_name}
COPY django.config /etc/unit/django.config

RUN --mount=type=cache,target=/var/cache/apt,sharing=locked \
    --mount=type=cache,target=/var/lib/apt,sharing=locked \
    rm -f /etc/apt/apt.conf.d/docker-clean; echo 'Binary::apt::APT::Keep-Downloaded-Packages "true";' > /etc/apt/apt.conf.d/keep-cache \
    && apt-get update -y \
    && apt-get install -y python3 \
    && apt-get -o APT::Install-Recommends=false upgrade -y \
    && mkdir -p {workdir}/{django_project_name}/static \
    && apt-get autoremove -y

RUN apt-get update \
    && apt-get install -y curl \
    && curl --output /usr/share/keyrings/nginx-keyring.gpg https://unit.nginx.org/keys/nginx-keyring.gpg \
    && echo "deb [signed-by=/usr/share/keyrings/nginx-keyring.gpg] https://packages.nginx.org/unit/debian/ bookworm unit" > /etc/apt/sources.list.d/unit.list \
    && apt-get update \
    && apt-get install -y unit unit-dev unit-python3.11

EXPOSE 8000

RUN . {workdir}/my_app_venv/bin/activate && {workdir}/my_app_venv/bin/python3 {workdir}/{django_project_name}/manage.py collectstatic --noinput && deactivate

RUN unitd --control unix:/var/run/control.unit.sock ;\
    curl -X PUT --data-binary @/etc/unit/django.config --unix-socket /run/control.unit.sock http://localhost/config

# Commande CMD corrigée
CMD ["unitd", "--no-daemon", "--control", "unix:/var/run/control.unit.sock"]
"""

# Écrire le contenu dans un fichier Dockerfile
with open("Dockerfile", "w") as dockerfile:
    dockerfile.write(dockerfile_content)

print("Fichier Dockerfile généré avec succès.")
