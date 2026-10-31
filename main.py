from fastapi import FastAPI

# On crée l'application
app = FastAPI()


# Quand on ouvre la page d'accueil "/", l'appli répond Hello World
@app.get("/")
def hello():
    return {"message": "Hello World"}