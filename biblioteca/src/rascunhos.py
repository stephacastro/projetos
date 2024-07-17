'''from datetime import datetime
import uuid
from datetime import datetime as dt

class Livro:
    def __init__(self, titulo: str, autor: str, genero: str, disponivel=True):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.disponivel = disponivel

    # informações dos livros adicionados
    def __str__(self):
        return f"Titulo: {self.titulo} \n Autor: {self.autor} \n Genero: {self.genero}"

class Usuario:
    def __init__(self, nome: str, user_id: str):
        self.id = user_id
        self.nome = nome

    def __str__(self):
        return f"ID: {self.id} \n Nome: {self.nome}"

class Emprestimo:
    def __init__(self, nome_livro:str, nome_usuario:str, id_usuario:str, data_emprestimo:datetime, data_devolucao:dt):
        self.nome_livro = nome_livro
        self.nome_usuario = nome_usuario
        self.id_usuario = id_usuario
        self.data_emprestimo = data_emprestimo
        self.data_devolucao  = data_devoulucao

# armazenar os livros e criar uma correlação entre livros e usuarios
class Biblioteca:
    def __init__(self, livro: Livro, usuario: Usuario, emprestimo:Emprestimo):
        self.usuario = usuario
        self.livro = livro
        self.usuarios = []
        self.livros = []
        self.emprestimos = []
        self.emprestimo = emprestimo

    def realizar_emprestimo(self, nome_livro: str, nome_usuario: str):
        # trazer um array com os livros emprestados
        # definir o maximo de emprestimo para 3 livros
        buscar_usuario = self.biblioteca.buscar_usuario(nome_usuario)
        buscar_livro = self.biblioteca.buscar_livro(nome_livro)

        if not buscar_usuario:
            raise Exception("")
        
        emprestimo = self.emprestimo(buscar_livro.titulo,buscar_usuario.nome, "data", "data")
        
        self.emprestimos.append(emprestimo)

    def multa(self):
        # calcular a multa quando passar de 5 dias da data que foi feito o emprestimo
        # multa de 10 reais por dia de atraso
        raise NotImplemented('Função precisa ser construida')

    def devolucao(self):
        if not self.livro.disponivel:
            self.livro.disponivel = True
            # definir data da devolucao 
            print(f'Livro "{self.livro.titulo}" devolvido por {self.usuario.usuario}.')
        else:
            print(f'Livro "{self.livro.titulo}" já está disponível.')

    def cadastrar_usuario(self):
        id_usuario = uuid.uuid1()
        nome = input("Usuário: ")

        lista_usuario = [usuario.nome.lower() for usuario in self.usuarios]

        if nome not in lista_usuario:
            novo_usuario = self.usuario(nome, id_usuario)
            self.usuarios.append(novo_usuario)
            print(f'Usuário "{nome}" cadastrado com sucesso.')
        else:
            print(f"{nome} já cadastrado.")

    def listar_usuarios(self):
        if not self.usuarios:
            print("Nenhum Usuário cadastrado.")
            return
        for usuario in self.usuarios:
            print(f"* id - {usuario.id} \n nome - {usuario.nome}")

    def buscar_usuario(self, nome_usuario: str):
        pass

    def cadastrar_livro(self):
        titulo = input("Titulo: ")
        autor = input("Autor: ")
        genero = input("Gênero: ")

        titulos = [livro.titulo.lower() for livro in self.livros]

        if titulo.lower() not in titulos:
            novo_livro = self.livro(titulo, autor, genero)
            self.livros.append(novo_livro)
            print(f"{titulo} adicionado com sucesso!")
        else:
            print("Livro já cadastrado na base de dados")

    def listar_livros(self):
        for livro in self.livros:
            print(f"Titulo - {livro.titulo} \n Autor - {livro.autor}")
            if not self.livros:
                print("Nenhum livro cadastrado.")
                return

    def buscar_livro(self, nome_livro: str):
        # implementar o buscar livro
        pass

    def remover_livro(self):
        remover_titulo = input("Qual o título do livro a ser removido: ")
        for livro in self.livros:
            if livro.titulo.lower() == remover_titulo.lower():
                self.livros.remove(livro)
                print(f"Livro {remover_titulo} removido com sucesso.")
                return
        print("Livro não encontrado.")

    def atualizar_livro(self):
        atualizar_livro = input("Qual o titulo do livro a ser atualizado: ")
        for livro in self.livros:
            if livro.titulo.lower() == atualizar_livro:
                novo_titulo = input("Novo título ou ENTER para manter: ")
                novo_autor = input("Novo autor ou ENTER para manter: ")
                novo_genero = input("Novo gênero ou ENTER para manter: ")

                if novo_titulo:
                    livro.titulo = novo_titulo
                if novo_autor:
                    livro.autor = novo_autor
                if novo_genero:
                    livro.genero = novo_genero

                print(f"Livro {atualizar_livro} atualizado com sucesso.")
                return
        print("Livro não encontrado.")

# criar um menu com as opcoes da biblioteca'''