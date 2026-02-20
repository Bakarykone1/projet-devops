# 1. Image de base (légère et sécurisée)
FROM python:3.9-slim

# 2. Définir le répertoire de travail dans le container
WORKDIR /app

# 3. Installer les dépendances système nécessaires pour psycopg2 (la DB)
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# 4. Copier d'abord le fichier des dépendances (optimisation du cache)
COPY requirements.txt .

# 5. Installer les bibliothèques Python
RUN pip install --no-cache-dir -r requirements.txt

# 6. Copier le reste du code de l'application
COPY . .

# 7. Exposer le port que l'application utilise
EXPOSE 5000

# 8. Commande de lancement
CMD ["python", "app.py"]