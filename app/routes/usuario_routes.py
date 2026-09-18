from fastapi import APIRouter
from pydantic import BaseModel
from app.controllers.usuario_controller import realizar_login

# Define um prefixo para organizar o Swagger (ex: http://127.0.0.1:8000/usuarios/login)
router = APIRouter(prefix="/usuarios", tags=["Login e Autenticação"])

# Define o formato esperado no corpo (body) da requisição
class LoginRequest(BaseModel):
    nome: str
    senha: str

@router.post("/login")
def login(dados_login: LoginRequest):
    # Envia os dados validados pelo Pydantic para a regra de negócio no controller
    resposta = realizar_login(dados_login.nome, dados_login.senha)
    return resposta