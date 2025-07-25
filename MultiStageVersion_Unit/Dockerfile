
# Étape 1 : Construction de l'environnement virtuel et installation des dépendances Django
FROM debian:stable-slim AS builder

RUN mkdir -p /home/app

# Installation des outils nécessaires
RUN rm -f /etc/apt/apt.conf.d/docker-clean; echo 'Binary::apt::APT::Keep-Downloaded-Packages "true";' > /etc/apt/apt.conf.d/keep-cache

RUN --mount=type=cache,target=/var/cache/apt,sharing=locked     --mount=type=cache,target=/var/lib/apt,sharing=locked     apt-get update -y     && apt-get -o APT::Install-Recommends=false upgrade -y     && apt-get install -y     python3     python3-venv     python3-pip ;     apt-get autoremove -y

# Création de l'environnement virtuel
RUN python3 -m venv /home/app/my_app_venv

# Copie des fichiers du projet Django dans le conteneur
COPY test_app/requirements.txt /home/app/requirements.txt

# Installation des dépendances Django dans l'environnement virtuel
RUN --mount=type=cache,target=/root/.cache     /home/app/my_app_venv/bin/pip install -r /home/app/requirements.txt     && /home/app/my_app_venv/bin/pip install uvicorn

# Étape 2 : Création du conteneur final
FROM debian:stable-slim

# Copier l'environnement virtuel depuis l'étape précédente
COPY --from=builder /home/app/my_app_venv /home/app/my_app_venv

# Définir les variables d'environnement
ENV PATH="/home/app/my_app_venv/bin:$PATH"

RUN mkdir -p /home/app/test_app

COPY test_app /home/app/test_app
COPY django.config /etc/unit/django.config

RUN --mount=type=cache,target=/var/cache/apt,sharing=locked     --mount=type=cache,target=/var/lib/apt,sharing=locked     rm -f /etc/apt/apt.conf.d/docker-clean; echo 'Binary::apt::APT::Keep-Downloaded-Packages "true";' > /etc/apt/apt.conf.d/keep-cache     && apt-get update -y     && apt-get install -y python3     && apt-get -o APT::Install-Recommends=false upgrade -y     && mkdir -p /home/app/test_app/static     && apt-get autoremove -y ;  apt-get update     && apt-get install -y curl     && curl --output /usr/share/keyrings/nginx-keyring.gpg https://unit.nginx.org/keys/nginx-keyring.gpg     && echo "deb [signed-by=/usr/share/keyrings/nginx-keyring.gpg] https://packages.nginx.org/unit/debian/ bookworm unit" > /etc/apt/sources.list.d/unit.list     && apt-get update     && apt-get install -y unit unit-dev unit-python3.11

EXPOSE 8000

RUN . /home/app/my_app_venv/bin/activate && /home/app/my_app_venv/bin/python3 /home/app/test_app/manage.py collectstatic --noinput && deactivate

RUN unitd --control unix:/var/run/control.unit.sock ;    curl -X PUT --data-binary @/etc/unit/django.config --unix-socket /run/control.unit.sock http://localhost/config

# Commande CMD corrigée
CMD ["unitd", "--no-daemon", "--control", "unix:/var/run/control.unit.sock"]
