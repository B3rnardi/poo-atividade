from fastapi import HTTPException
from app.models.usuario import carregar_usuarios

def realizar_login(nome_tentativa: str, senha_tentativa: str):
    # Carrega a lista de objetos (já instanciados como Visitante, Contribuidor ou Moderador)
    usuarios_cadastrados = carregar_usuarios()
    
    for usuario in usuarios_cadastrados:
        # Valida o nome e usa o método público para validar a senha sem expor o atributo privado
        if usuario.mostrar_nome() == nome_tentativa and usuario.verificar_senha(senha_tentativa):
            return {
                "mensagem": "Login aprovado",
                "usuario": usuario.mostrar_nome(),
                # Polimorfismo: o Python sabe chamar a lista certa dependendo de qual classe filha o objeto é
                "permissoes": usuario.listar_permissoes()
            }
            
    # Se percorrer toda a lista e não encontrar correspondência, devolve erro 401
    raise HTTPException(status_code=401, detail="Credenciais inválidas")