# Utiliser une image de base Python
FROM python:3.8-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers de requirements et installer les dépendances
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copier le reste des fichiers de l'application
COPY app.py .

# Copier le fichier init.sql dans le conteneur
COPY init.sql /docker-entrypoint-initdb.d/

# Exposer le port sur lequel l'application s'exécutera
EXPOSE 5000
EXPOSE 5434

# Définir la commande pour démarrer l'application avec Gunicorn
CMD ["python", "app.py"]