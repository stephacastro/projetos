from src.models.usuario import Usuario
from src.models.livro import Livro
from src.models.emprestimo import Emprestimo
from datetime import datetime
import uuid
from typing import Optional

class Biblioteca:
    def __init__(self):
        self.usuarios = []
        self.livros = []
        self.emprestimos = []

    def realizar_emprestimo(self, nome_livro: str, nome_usuario: str):
        usuario = self.buscar_usuario(nome_usuario)
        livro = self.buscar_livro(nome_livro)

        if not usuario:
            raise Exception("Usuário não encontrado.")
        if not livro:
            raise Exception("Livro não encontrado.")
        if not livro.disponivel:
            raise Exception("Livro não está disponível para empréstimo.")
        if len([emp for emp in self.emprestimos if emp.id_usuario == usuario.id and (datetime.now() - emp.data_emprestimo).days <= 30]) >= 3:
            raise Exception("Usuário já possui 3 livros emprestados.")

        data_emprestimo = datetime.now()
        data_devolucao = data_emprestimo.replace(day=data_emprestimo.day + 7)
        emprestimo = Emprestimo(livro.titulo, usuario.nome, usuario.id, data_emprestimo, data_devolucao)

        self.emprestimos.append(emprestimo)
        livro.disponivel = False


    def multa(self):
        for emprestimo in self.emprestimos:
            dias_atraso = (datetime.now() - emprestimo.data_devolucao).days
            if dias_atraso > 0:
                multa = dias_atraso * 10
                print(f"Usuário {emprestimo.nome_usuario} tem uma multa de R${multa} pelo livro {emprestimo.nome_livro}.")


    def devolucao(self, nome_livro: str):
        emprestimo = next((emp for emp in self.emprestimos if emp.nome_livro == nome_livro), None)
        if emprestimo:
            livro = self.buscar_livro(nome_livro)
            livro.disponivel = True
            self.emprestimos.remove(emprestimo)
            print(f'Livro "{nome_livro}" devolvido por {emprestimo.nome_usuario}.')
        else:
            print(f'O livro "{nome_livro}" não está emprestado.')


    def cadastrar_usuario(self, nome: str):
        if nome.lower() in [usuario.nome.lower() for usuario in self.usuarios]:
            print(f"{nome} já cadastrado.")
            return
        novo_usuario = Usuario(nome)
        self.usuarios.append(novo_usuario)
        print(f'Usuário "{nome}" cadastrado com sucesso.')


    def listar_usuarios(self):
        if not self.usuarios:
            print("Nenhum usuário cadastrado.")
            return
        for usuario in self.usuarios:
            print(f"ID: {usuario.id} \nNome: {usuario.nome}")
            print('##########################################')



    def buscar_usuario(self, nome_usuario: str):
        return next((usuario for usuario in self.usuarios if usuario.nome.lower() == nome_usuario.lower()), None)


    def cadastrar_livro(self, titulo: str, autor: str, genero: str):
        if titulo.lower() in [livro.titulo.lower() for livro in self.livros]:
            print("Livro já cadastrado na base de dados")
            return
        novo_livro = Livro(titulo, autor, genero)
        self.livros.append(novo_livro)
        print(f'{titulo} adicionado com sucesso!')


    def listar_livros(self):
        if not self.livros:
            print("Nenhum livro cadastrado.")
            return
        for livro in self.livros:
            print(f"Titulo: {livro.titulo} \nAutor: {livro.autor}")
            print('##########################################')


    def buscar_livro(self, nome_livro: str):
        return next((livro for livro in self.livros if livro.titulo.lower() == nome_livro.lower()), None)

    def remover_livro(self, titulo: str):
        livro = self.buscar_livro(titulo)
        if livro:
            self.livros.remove(livro)
            print(f"Livro {titulo} removido com sucesso.")
        else:
            print("Livro não encontrado.")


    def atualizar_livro(self, titulo: str, novo_titulo: Optional[str] = None, novo_autor: Optional[str] = None, novo_genero: Optional[str] = None):
        livro = self.buscar_livro(titulo)
        if livro:
            if novo_titulo is not None:
                livro.titulo = novo_titulo
            if novo_autor is not None:
                livro.autor = novo_autor
            if novo_genero is not None:
                livro.genero = novo_genero
            print(f"Livro {titulo} atualizado com sucesso.")
        else:
            print("Livro não encontrado.")