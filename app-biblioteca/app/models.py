from sqlalchemy import Boolean, Column, ForeignKey, Integer, String #type:ignore
from sqlalchemy.orm import relationship #type:ignore

from app.database import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True)
    email = Column(String(150), unique=True, index=True)
    usuario = Column(String(150), unique=True, index=True)
    senha = Column(String(150))
    ativo = Column(Boolean, default=True)

class Livro(Base):
    __tablename__ = "livros"

    id = Column(Integer, primary_key=True)
    titulo = Column(String(150), index=True)
    autor = Column(String(150), index=True)
    genero = Column(String(15), index=True)
    disponivel = Column(Boolean, default=True)