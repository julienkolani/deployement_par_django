import os

def get_project_choice(project_files):
    while True:
        try:
            choice = int(input("Choisissez un numéro de projet (1, 2, ...) : "))
            if 1 <= choice <= len(project_files):
                return project_files[choice - 1]
            else:
                print("Choix invalide. Veuillez choisir un numéro valide.")
        except ValueError:
            print("Veuillez entrer un numéro valide.")

def generate_dockerfile(python_version, workdir, django_project_name):
    dockerfile_content = f"""
FROM python:{python_version}

ENV workdir={workdir}
ENV DJANGO_PROJECT_NAME={django_project_name}

RUN mkdir -p {workdir}/{django_project_name}

COPY {django_project_name} {workdir}/{django_project_name}

RUN apt-get update && \\
    mkdir -p {workdir}/{django_project_name}/static; \\
    pip install --upgrade pip && \\
    pip install -r {workdir}/{django_project_name}/requirements.txt && \\
    pip install uvicorn

EXPOSE 8000

CMD ["bash", "-c", "cd {workdir}/{django_project_name} && uvicorn {django_project_name}.asgi:application --host 0.0.0.0 --port 8000"]
"""
    return dockerfile_content

def main():
    # Obtenir la liste des fichiers du répertoire courant
    current_directory = os.getcwd()
    project_files = [f for f in os.listdir(current_directory) if os.path.isdir(f)]

    # Afficher la liste des projets disponibles
    print("Projets disponibles dans le répertoire courant:")
    for i, project in enumerate(project_files, start=1):
        print(f"{i}. {project}")

    # Demander à l'utilisateur de choisir un projet
    chosen_project = get_project_choice(project_files)

    # Variables
    python_version = "3.9.18-slim-bullseye"
    workdir = "/home/app"

    # Générer le contenu du Dockerfile
    dockerfile_content = generate_dockerfile(python_version, workdir, chosen_project)

    # Écrire le contenu dans un fichier Dockerfile
    with open("Dockerfile", "w") as dockerfile:
        dockerfile.write(dockerfile_content)

    print("Fichier Dockerfile généré avec succès.")

if __name__ == "__main__":
    main()
