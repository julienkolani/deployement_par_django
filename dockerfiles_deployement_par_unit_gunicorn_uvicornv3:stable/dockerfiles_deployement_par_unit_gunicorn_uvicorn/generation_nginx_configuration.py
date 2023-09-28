# Variables à personnaliser
listen_port = 8000  # Port d'écoute de Nginx
ip_address = "192.168.1.100"  # Adresse IP de l'application Django
domain_name = "example.com"  # Nom de domaine de l'application Django

# Modèle de configuration Nginx
nginx_config = f"""server {{
    listen {listen_port};
    server_name {domain_name};

    location /static/ {{
        proxy_pass http://{ip_address}:{listen_port};
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }}

    location / {{
        proxy_pass http://{ip_address}:{listen_port};
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }}
}}
"""

# Enregistrer la configuration dans un fichier
with open("nginx_config.conf", "w") as config_file:
    config_file.write(nginx_config)

print("Configuration Nginx générée avec succès dans le fichier nginx_config.conf.")
