from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


# MY Test
def test_my_test():
    # On ouvre la page d'accueil
    reponse = client.get("/")

    # La page doit marcher (200 = OK)
    assert reponse.status_code == 200

    # La page doit afficher Hello World
    assert reponse.json() == {"message": "Hello World"}