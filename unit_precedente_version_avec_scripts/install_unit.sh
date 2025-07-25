#!/bin/bash

# Installer les paquets nécessaires : curl, systemctl
apt update
apt install -y curl systemd

# Télécharger la clé GPG du référentiel NGINX Unit et l'ajouter au trousseau
curl --output /usr/share/keyrings/nginx-keyring.gpg https://unit.nginx.org/keys/nginx-keyring.gpg

# Ajouter les sources du référentiel NGINX Unit au fichier sources.list
echo "deb [signed-by=/usr/share/keyrings/nginx-keyring.gpg] https://packages.nginx.org/unit/debian/ bookworm unit" > /etc/apt/sources.list.d/unit.list
echo "deb-src [signed-by=/usr/share/keyrings/nginx-keyring.gpg] https://packages.nginx.org/unit/debian/ bookworm unit" >> /etc/apt/sources.list.d/unit.list

# Mettre à jour la liste des paquets
apt update

# Installer NGINX Unit et les modules associés
apt install -y unit unit-dev unit-python3.11

# Redémarrer le service NGINX Unit
systemctl restart unit
