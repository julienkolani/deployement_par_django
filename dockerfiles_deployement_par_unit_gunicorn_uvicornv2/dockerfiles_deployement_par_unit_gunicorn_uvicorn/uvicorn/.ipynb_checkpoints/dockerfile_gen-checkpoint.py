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

# Création du contenu du Dockerfile
dockerfile_content = f"""
FROM python:{python_version}

RUN mkdir -p {workdir}/{django_project_name}

COPY {django_project_name} {workdir}/{django_project_name}

# Installation des outils nécessaires

RUN rm -f /etc/apt/apt.conf.d/docker-clean; echo 'Binary::apt::APT::Keep-Downloaded-Packages "true";' > /etc/apt/apt.conf.d/keep-cache

RUN --mount=type=cache,target=/var/cache/apt,sharing=locked \
    --mount=type=cache,target=/var/lib/apt,sharing=locked \
    --mount=type=cache,target=/root/.cache \
    apt-get update -y; \  
    apt-get update --no-cache-dir -y; \
    apt-get -o APT::Install-Recommends=false upgrade; \
    mkdir -p {workdir}/{django_project_name}/static; \
    pip install --upgrade pip && \
    pip install -r {workdir}/{django_project_name}/requirements.txt && \
    pip install uvicorn && \
    python3 {workdir}/{django_project_name}/manage.py collectstatic --noinput
    
RUN apt-get remove --purge pip && \
    apt-get autoremove

EXPOSE 8000

CMD ["bash", "-c", f"cd {workdir}/{django_project_name} && uvicorn {django_project_name}.asgi:application --host 0.0.0.0 --port 8000"]
"""

# Écrire le contenu dans un fichier Dockerfile
with open("Dockerfile", "w") as dockerfile:
    dockerfile.write(dockerfile_content)

print("Fichier Dockerfile généré avec succès.")
