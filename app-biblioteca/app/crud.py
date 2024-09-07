from sqlalchemy.orm import Session
from sqlalchemy import create_engine, Column, Integer, Boolean
from app import models, schemas

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

def usuario_por_email(db: Session, email:str):
    return db.query(models.Usuario).filter(models.Usuario.email == email).first()