import os

# Définir la valeur de workdir (chemin du répertoire de l'application)
workdir = "/home/app"

# Obtenir la liste des fichiers du répertoire courant
current_directory = os.getcwd()
project_files = [f for f in os.listdir(current_directory) if os.path.isdir(f)]

# Afficher la liste des projets disponibles
print("******************** Entrez le nom de l'application Django ********************")

print("Projets disponibles dans le répertoire courant:\n")
for i, project in enumerate(project_files, start=1):
    print(f"{i}. {project}")

# Demander à l'utilisateur de choisir un projet
while True:
    try:
        choice = int(input("Choisissez un numéro de projet (1, 2, ...) : "))
        if 1 <= choice <= len(project_files):
            app_name = project_files[choice - 1]
            break
        else:
            print("Choix invalide. Veuillez choisir un numéro valide.")
    except ValueError:
        print("Veuillez entrer un numéro valide.")

# Modèle de configuration
CONFIG_TEMPLATE = f"""{{
    "listeners": {{
        "*:8000": {{
            "pass": "routes"
        }}
    }},
    "routes": [
        {{
            "match": {{
                "uri": "/static/*"
            }},
            "action": {{
                "share": "{workdir}/{app_name}/staticfiles/$uri"
            }}
        }},
        {{
            "action": {{
                "pass": "applications/{app_name}"
            }}
        }}
    ],
    "applications": {{
        "{app_name}": {{
            "type": "python",
            "processes": 5,
            "module": "{app_name}.wsgi",
            "path": "{workdir}/{app_name}",
            "home": "{workdir}/my_app_venv/"
        }}
    }}
}}
"""

def generate_django_config(app_name, process):
    # Remplacer les valeurs dans le modèle de configuration
    config = CONFIG_TEMPLATE

    with open(f"django.config", "w") as config_file:
        config_file.write(config)

if __name__ == "__main__":
    process = 5
    generate_django_config(app_name, process)
    print(f"Fichier django.config généré avec succès.")
