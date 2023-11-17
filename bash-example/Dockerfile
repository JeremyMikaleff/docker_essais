FROM python:3-alpine
WORKDIR /app


# Créer un environnement virtuel dans le répertoire /venv
RUN python -m venv /venv

# Activer l'environnement virtuel
ENV PATH="/venv/bin:$PATH"

ENV NOM_USER="mikaleff"
ENV PRENOM_USER="jeremy"

# Mettre à jour pip
RUN pip install --upgrade pip

RUN pip install requests

# Copie le script dans le conteneur, dans le répertoire /app
COPY script.sh script-hello-world.sh
COPY nom_prenom.py nom_prenom.py

CMD ["python", "/app/nom_prenom.py"]

# Exemple de commande HEALTHCHECK (à ajuster selon vos besoins)
HEALTHCHECK --interval=10s --timeout=3s \
    CMD python -c 'import requests; response = requests.get("https://www.google.com"); assert response.status_code == 200'