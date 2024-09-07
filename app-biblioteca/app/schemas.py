from pydantic import BaseModel


class UsuarioBase(BaseModel):
    email: str
class CriarUsuario(UsuarioBase):
    usuario: str
    senha: str