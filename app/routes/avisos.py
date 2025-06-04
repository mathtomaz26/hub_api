from fastapi import APIRouter, Depends
from app.db import db
from app.auth import validar_token

router = APIRouter(prefix="/avisos", tags=["Avisos"])

@router.get("/", dependencies=[Depends(validar_token)])
def listar_avisos():
    dados = list(db["avisos"].find({}, {"_id": 0}))
    return dados
