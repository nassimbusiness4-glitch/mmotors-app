# On part d'une image qui contient déjà Python
FROM python:3.14-slim

# On travaille dans le dossier /app
WORKDIR /app

# On copie nos fichiers dans l'image
COPY . .

# On installe les outils de la liste
RUN pip install -r requirements.txt

# L'appli écoute sur le port 8000
EXPOSE 8000

# La commande pour démarrer l'appli
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]