def print_title(title):
    print(f"\n{title}\n{'=' * len(title)}")

def unit_procedure():
    print_title("Procedure de déploiement UNIT :")
    print("1. Copier le fichier ./run.sh, dockerfile_gen.py et le projet dans le même répertoire.")
    print("2. Modifier le fichier settings.py pour avoir :")
    print('''  
            import os
            import socket

            DEBUG = False
                        
            ip1 = socket.gethostbyname(socket.gethostname())
            ip2 = os.environ.get("hostname", "www.example.com")
                        
            ALLOWED_HOSTS = [ip1, ip2]
            ''')
    print("3. Vérifier si tout est en place avec Procedure_deployement.py.")
    print("4. Générer le Dockerfile.")
    print("5. Lancer la création de l'image Docker avec :")
    print("   docker build -t nom_container .")
    print("6. Lancer l'image pour avoir un container avec :")
    print("   docker run --name nom_container -p 8001:8000 nom_image:version")

def gunicorn_uvicorn_procedure():
    print_title("Procedure de déploiement GUNICORN UVICORN :")
    print("1. Modifier le fichier settings.py pour avoir :")
    print('''  
            import os
            import socket

            DEBUG = False
                        
            ip1 = socket.gethostbyname(socket.gethostname())
            ip2 = os.environ.get("hostname", "www.example.com")
                        
            ALLOWED_HOSTS = [ip1, ip2]
            ''')
    print("2. Vérifier si tout est en place avec Procedure_deployement.py.")
    print("3. Générer le Dockerfile d'après le bon script, soit uvicorn ou gunicorn.")
    print("4. Lancer la création de l'image Docker avec :")
    print("   docker build -t nom_container .")
    print("5. Lancer l'image pour avoir un container avec :")
    print("   docker run --name nom_container -p 8001:8000 nom_image:version")

if __name__ == "__main__":
    print_title("Bienvenue dans l'assistant de déploiement")
    print("""
    
        Warning : Les Dockerfiles utilisent : 
        
            --mount=type=cache,target=/var/cache/apt,sharing=locked \\
            --mount=type=cache,target=/var/lib/apt,sharing=locked \\
            --mount=type=cache,target=/root/.cache \\
    
        Assurez-vous donc d'avoir installé : docker-buildx et d'avoir ajouté : export DOCKER_BUILDKIT=1 aux variables d'environnement !
    """)
    print("Choisissez une procédure de déploiement :\n")
    print("1. UNIT")
    print("2. GUNICORN UVICORN\n")
    
    choice = input("Votre choix (1/2) : ")

    if choice == "1":
        unit_procedure()
    elif choice == "2":
        gunicorn_uvicorn_procedure()
    else:
        print("Choix invalide. Veuillez choisir 1 ou 2.")
