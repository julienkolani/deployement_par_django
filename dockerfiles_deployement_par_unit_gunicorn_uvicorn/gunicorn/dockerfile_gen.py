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
python_version = "3.9.18-slim-bullseye"
workdir = "/home/app"

# Créer le contenu du Dockerfile
dockerfile_content = f"""
FROM python:{python_version}

ENV workdir={workdir}
ENV DJANGO_PROJECT_NAME={django_project_name}

RUN mkdir -p /home/app/{django_project_name}

COPY {django_project_name} /home/app/{django_project_name}

COPY get_ip_address.py /home/app/{django_project_name}/{django_project_name}

RUN apt-get update && \\
    mkdir -p /home/app/{django_project_name}/static; \\
    pip install --upgrade pip && \\
    pip install -r /home/app/{django_project_name}/requirements.txt && \\
    pip install gunicorn && \\
    python3 /home/app/{django_project_name}/manage.py collectstatic --noinput

EXPOSE 8000

CMD ["python3", "-m", "gunicorn", "-b", "0.0.0.0:8000", "--chdir", "/home/app/{django_project_name}", "-k", "sync", "{django_project_name}.wsgi:application"]
"""

# Écrire le contenu dans un fichier Dockerfile
with open("Dockerfile", "w") as dockerfile:
    dockerfile.write(dockerfile_content)

print("Fichier Dockerfile généré avec succès.")
