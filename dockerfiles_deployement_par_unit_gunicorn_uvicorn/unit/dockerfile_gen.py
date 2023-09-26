import os

# Fonction pour obtenir le choix valide de l'utilisateur
def get_valid_choice(options):
    while True:
        try:
            choice = int(input("Choisissez un numéro de projet (1, 2, ...) : "))
            if 1 <= choice <= len(options):
                return choice
            else:
                print("Choix invalide. Veuillez choisir un numéro valide.")
        except ValueError:
            print("Veuillez entrer un numéro valide.")

# Obtenir la liste des fichiers du répertoire courant
current_directory = os.getcwd()
project_files = [f for f in os.listdir(current_directory) if os.path.isdir(f)]

# Afficher la liste des projets disponibles
print("Projets disponibles dans le répertoire courant:")
for i, project in enumerate(project_files, start=1):
    print(f"{i}. {project}")

# Demander à l'utilisateur de choisir un projet
choice = get_valid_choice(project_files)
django_project_name = project_files[choice - 1]

# Variables
python_version = "3.11"
workdir = "/home/app"

# Créer le contenu du Dockerfile
dockerfile_content = f"""
FROM unit:python{python_version}

ENV workdir={workdir}
ENV DJANGO_PROJECT_NAME={django_project_name}

RUN mkdir -p /home/app/{django_project_name}

COPY {django_project_name} /home/app/{django_project_name}

COPY django.config /etc/unit/django.config

COPY run.sh /run.sh

RUN chmod +x /run.sh && \\
    apt-get update && \\
    pip install --upgrade pip && \\
    pip install -r /home/app/{django_project_name}/requirements.txt

EXPOSE 8000

CMD ["./run.sh"]
"""

# Écrire le contenu dans un fichier Dockerfile
with open("Dockerfile", "w") as dockerfile:
    dockerfile.write(dockerfile_content)

print("Fichier Dockerfile généré avec succès.")
