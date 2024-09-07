from app.database import SessionLocal, engine
from fastapi import FastAPI, Depends, HTTPException, status #type:ignore
from app.database import get_db
from app import models, schemas, crud
from sqlalchemy.orm import Session #type:ignore
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:5173",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/boas-vindas")
async def boas_vindas():
    return 'Testando API'

@app.post("/usuario/", response_model=schemas.CriarUsuario)
def criar_usuario(usuario: schemas.CriarUsuario, db: Session = Depends(get_db)):
    db_usuario = crud.usuario_por_email(db, email=usuario.email)
    if db_usuario:
        raise HTTPException(status_code=400, detail="Usuário já cadastrado")
    return crud.criar_usuario(db=db, usuario=usuario)