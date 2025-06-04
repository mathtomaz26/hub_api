from fastapi import FastAPI
from app.routes import associados, cobranca, avisos

app = FastAPI()

app.include_router(associados.router)
app.include_router(cobranca.router)
app.include_router(avisos.router)

@app.get("/")
def root():
    return {"status": "API ativa"}
