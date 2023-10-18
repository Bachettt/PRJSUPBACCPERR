# Utiliser une image de base Python
FROM python:3.8-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers de requirements et installer les dépendances
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copier le reste des fichiers de l'application
COPY . .

# Exposer le port sur lequel l'application s'exécutera
EXPOSE 5000

# Définir la commande pour démarrer l'application
CMD ["flask", "run", "--host=0.0.0.0"]

