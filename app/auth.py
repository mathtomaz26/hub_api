from fastapi import Header, HTTPException
import os

def validar_token(authorization: str = Header(...)):
    token_esperado = f"Bearer {os.getenv('API_TOKEN')}"
    if authorization != token_esperado:
        raise HTTPException(status_code=401, detail="Token inválido")
