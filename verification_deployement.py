# Liste des étapes de mise en production avec des explications
etapes = [
    ("Créer le fichier requirement.txt", "Créez un fichier requirement.txt pour répertorier les dépendances Python de votre projet Django. Ces dépendances seront installées lors du déploiement."),
    ("Collecter les fichiers statiques", "Utilisez la commande `collectstatic` pour rassembler les fichiers statiques de votre application Django. Ces fichiers sont nécessaires pour servir les ressources statiques telles que les images, les feuilles de style et les scripts."),
    ("Créer les fichiers .env", "Créez des fichiers .env pour stocker des variables d'environnement comme les clés secrètes, les informations de base de données et d'autres paramètres sensibles."),
    ("Configurer le nom de domaine ou l'IP du container dans allowed hosts", "Ajoutez le nom de domaine ou l'adresse IP du serveur dans la liste des allowed hosts de votre application Django. Cela permet à l'application d'accepter les requêtes provenant de ce domaine ou de cette IP."),
    ("Choix de la solution de déploiement", "Choisissez la solution de déploiement qui convient le mieux à votre projet, que ce soit un serveur dédié, un service de cloud ou un conteneur Docker."),
    ("Mettre le projet dans le même répertoire que le bon Dockerfile", "Assurez-vous que votre projet Django est correctement organisé dans le même répertoire que le fichier Dockerfile approprié, si vous utilisez Docker pour le déploiement."),
    ("Configuration de la base de données", "Configurez une base de données compatible avec Django, comme PostgreSQL ou MySQL, sur le serveur de déploiement. Adaptez les paramètres Django pour qu'ils correspondent à la configuration de la base de données."),
    ("Paramètres de sécurité - Vérifier si aucune donnée importante n'est dans le settings.py", "Assurez-vous qu'aucune information sensible, telle que des clés secrètes ou des informations de base de données, ne se trouve directement dans le fichier settings.py de votre projet Django. Utilisez des variables d'environnement pour stocker ces informations de manière sécurisée."),
    ("Configuration du serveur web proxy Nginx", "Configurez un serveur web proxy comme Nginx pour gérer les requêtes HTTP et les rediriger vers l'application Django via un serveur WSGI comme Gunicorn ou uWSGI. Cela permet de servir votre application de manière efficace et sécurisée.")
]

# Liste des étapes indispensables
etapes_indispensables = [1, 2, 5, 6, 7]

# Liste pour stocker les étapes non validées
etapes_non_validees = []

# Affichage des étapes avec des explications
print("Étapes de mise en production :")
print("-----------------------------")
for i, (etape, explication) in enumerate(etapes, start=1):
    while True:
        reponse = input(f"{i}. Avez-vous terminé l'étape '{etape}' ? (o/n): ").strip().lower()
        if reponse == 'o':
            break
        elif reponse == 'n':
            etapes_non_validees.append((i, etape))
            break
        else:
            print("Réponse invalide. Veuillez entrer 'o' pour Oui ou 'n' pour Non.")

# Vérification des étapes indispensables
etapes_indispensables_non_validees = [etape for etape in etapes_indispensables if etape in [i for i, _ in etapes_non_validees]]

# Affichage des résultats avec des explications
print("\nRésultats :")
print("------------")
if etapes_indispensables_non_validees:
    print("Erreur : Toutes les étapes indispensables n'ont pas été validées. Le déploiement ne peut pas être effectué.")
    print("Tâches non validées :")
    for i, etape in etapes_non_validees:
        print(f"{i}. {etape}")
elif etapes_non_validees:
    print("Avertissement : Toutes les étapes n'ont pas été validées. Le déploiement peut être effectué, mais certaines tâches restent à compléter.")
    print("Tâches non validées :")
    for i, etape in etapes_non_validees:
        print(f"{i}. {etape}")
else:
    print("Toutes les tâches ont été validées. Le déploiement peut être effectué avec succès.")
