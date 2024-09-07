from app.database import SessionLocal, engine
from fastapi import FastAPI, Depends, HTTPException, status #type:ignore
from app.database import get_db
from app import models, schemas, crud
from sqlalchemy.orm import Session #type:ignore
from fastapi.middleware.cors import CORSMiddleware #type:ignore

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
    return {'mensagem': 'Testando API'}

@app.post("/usuarios/", response_model=schemas.Usuario)
def criar_usuario(usuario: schemas.CriarUsuario, db: Session = Depends(get_db)):
    db_usuario = crud.usuario_por_email(db, email=usuario.email)
    if db_usuario:
        raise HTTPException(status_code=400, detail="Usuário já cadastrado")
    return crud.criar_usuario(db=db, usuario=usuario)

@app.post("/usuarios/{id}", response_model=schemas.Usuario)
def pegar_usuario_existente_por_id(id: int, db: Session = Depends(get_db)):
    db_usuario = crud.pegar_usuario(db, id=id)
    if db_usuario is None:
        raise HTTPException(status_code=400, detail="Usuário não encontrado")
    return db_usuario

# rota com erro para cadastrar o livro
@app.post("/livros/", response_model=schemas.Livro)
def cadastrar_livro(livro: schemas.Cadastrar_livro, db: Session = Depends(get_db)):
    db_livro = crud.pegar_livro(db, titulo=livro.titulo)
    print(f">>>>>>> {db_livro}")
    if db_livro:
        raise HTTPException(status_code=400, detail="Livro já cadastrado")
    return db_livro




@app.post("/livros/{id}", response_model=schemas.Livro)
def pegar_livro_por_id(id:int, db: Session = Depends(get_db)):
    db_livro = crud.pegar_livro_id(db, id=id)
    print(db_livro)
    if db_livro is None:
        raise HTTPException(status_code=400, detail="Livro não encontrado")
    return  db_livro