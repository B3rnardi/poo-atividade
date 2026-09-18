from fastapi import APIRouter
from pydantic import BaseModel
from app.controllers.usuario_controller import realizar_login

router = APIRouter(prefix="/usuarios", tags=["Login e Autenticação"])

class LoginRequest(BaseModel):
    nome: str
    senha: str

@router.post("/login")
def login(dados_login: LoginRequest):
    resposta = realizar_login(dados_login.nome, dados_login.senha)
    return resposta