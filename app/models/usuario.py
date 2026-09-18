from app.data.usuarios_mock import USUARIOS

class Usuario:
    def __init__(self, id, nome, senha):
        self._id = id
        self._nome = nome
        self.__senha = senha  # Encapsulamento: atributo estritamente privado

    def mostrar_id(self):
        return self._id

    def mostrar_nome(self):
        return self._nome

    # Método público para validar a palavra-passe de forma segura sem a expor
    def verificar_senha(self, senha_tentativa):
        return self.__senha == senha_tentativa

    # Método base que será sobrescrito (Polimorfismo)
    def listar_permissoes(self):
        return []


class Visitante(Usuario):
    def listar_permissoes(self):
        return ["visualizar_ofertas"]


class Contribuidor(Usuario):
    def listar_permissoes(self):
        return ["visualizar_ofertas", "criar_ofertas"]


class Moderador(Usuario):
    def listar_permissoes(self):
        return ["visualizar_ofertas", "criar_ofertas", "editar_ofertas", "excluir_ofertas", "gerir_utilizadores"]


# Dica do professor: mapeamento de string para a Classe real
PERFIS = {
    'visitante': Visitante,
    'contribuidor': Contribuidor,
    'moderador': Moderador
}

def carregar_usuarios():
    usuarios_instanciados = []
    for u in USUARIOS:
        # 1. Identifica a classe correta através do texto do mock
        classe_do_usuario = PERFIS[u['perfil']]
        
        # 2. Instancia o objeto da classe filha correspondente
        usuario_obj = classe_do_usuario(u['id'], u['nome'], u['senha'])
        
        usuarios_instanciados.append(usuario_obj)
        
    return usuarios_instanciados