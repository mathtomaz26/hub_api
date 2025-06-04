from fastapi import APIRouter, Depends
from app.db import db
from app.auth import validar_token

router = APIRouter(prefix="/associados", tags=["Associados"])

@router.get("/", dependencies=[Depends(validar_token)])
def listar_associados():
    dados = list(db["associados"].find({}, {"_id": 0}))
    return dados
