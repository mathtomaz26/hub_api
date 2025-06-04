from fastapi import APIRouter, Depends
from app.db import db
from app.auth import validar_token

router = APIRouter(prefix="/cobranca", tags=["Cobrança"])

@router.get("/", dependencies=[Depends(validar_token)])
def listar_cobranca():
    dados = list(db["cobranca"].find({}, {"_id": 0}))
    return dados
