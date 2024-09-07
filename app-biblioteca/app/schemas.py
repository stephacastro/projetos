from pydantic import BaseModel #type:ignore


class UsuarioBase(BaseModel):
    email: str
class CriarUsuario(UsuarioBase):
    usuario: str
    senha: str

class Usuario(UsuarioBase):
    id: int
    ativo: bool

class BaseLivro(BaseModel):
    titulo: str

class Cadastrar_livro(BaseLivro):
    autor: str
    gereno: str

class Livro(BaseLivro):
    id: int
    disponivel: bool