from fastapi import HTTPException
from app.models.usuario import carregar_usuarios

def realizar_login(nome_tentativa: str, senha_tentativa: str):
    usuarios_cadastrados = carregar_usuarios()
    
    for usuario in usuarios_cadastrados:
        if usuario.mostrar_nome() == nome_tentativa and usuario.verificar_senha(senha_tentativa):
            return {
                "mensagem": "Login aprovado",
                "usuario": usuario.mostrar_nome(),
                "permissoes": usuario.listar_permissoes()
            }
            
    raise HTTPException(status_code=401, detail="Credenciais inválidas")