from sqlalchemy.orm import Session #type:ignore
from sqlalchemy import create_engine, Column, Integer, Boolean #type:ignore
from app import models, schemas #type:ignore

def criar_usuario(db: Session, usuario:schemas.CriarUsuario):
    db_usuario = models.Usuario(
        email=usuario.email,
        usuario=usuario.usuario,
        senha=usuario.senha
    )
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

def cadastrar_livro(db: Session, livro:schemas.Cadastrar_livro):
    db_livro = models.Livro(
        titulo=livro.titulo,
        autor=livro.autor,
        genero=livro.gereno
    )
    db.add(db_livro)
    db.commit()
    db.refresh(db_livro)
    return db_livro

def pegar_livro(db: Session, titulo:str):
    return db.query(models.Livro).filter(models.Livro.titulo == titulo).first()

def pegar_livro_id(db: Session, id:int):
    return db.query(models.Livro).filter(models.Livro.id == id).first()

def usuario_por_email(db: Session, email:str):
    return db.query(models.Usuario).filter(models.Usuario.email == email).first()

def pegar_usuario(db: Session, id:int):
    return db.query(models.Usuario).filter(models.Usuario.id == id).first()