import os
import requests
import time

while True:
    print(f"Le conteneur de {os.environ['PRENOM_USER']} {os.environ['NOM_USER']} est en cours d'exécution...")
    print(requests.get('https://www.google.com'))
    time.sleep(10)