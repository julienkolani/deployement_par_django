# 🚀 Django Deployment Benchmark (Gunicorn, Uvicorn, Nginx Unit)

Ce projet est un banc de test pour comparer **trois méthodes de déploiement d'une application Django** dans des environnements Docker, en utilisant respectivement :
- Gunicorn
- Uvicorn
- Nginx Unit

L'objectif est de mesurer et comparer les performances (CPU, RAM, temps de réponse) de ces solutions sous charge, afin de déterminer laquelle est la plus efficace pour un environnement de production léger ou embarqué.

---

## 📦 Objectifs du projet

- Déployer la même application Django via trois stacks différentes
- Simuler du trafic via `wrk` ou un autre outil de stress test
- Analyser les performances en termes de :
  - Consommation CPU
  - Consommation RAM
  - Temps de réponse
- Déterminer la solution la plus performante et stable

---

## ⚙️ Stack technique

- **Django** (application de base identique pour chaque test)
- **Docker** (chaque stack dans un conteneur séparé)
- **Serveurs testés** :
  - [Gunicorn](https://gunicorn.org/)
  - [Uvicorn](https://www.uvicorn.org/) (avec ASGI)
  - [Nginx Unit](https://unit.nginx.org/)
- **Outils de benchmark** : `wrk`, `ab`, ou équivalent
- **Surveillance** : `htop`, `docker stats`, outils custom


---

## Conclusion provisoire
Lors de mes tests, Nginx Unit a montré les meilleures performances globales en termes de RAM et de temps de réponse, tout en ayant une configuration relativement simple pour Django. Gunicorn reste une valeur sûre, mais consomme un peu plus. Uvicorn est rapide, mais semble moins stable sous forte charge sans supervision externe.