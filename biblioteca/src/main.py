from datetime import datetime
import uuid
from typing import Optional

# CONSTRUÇÃO DAS CLASSES 

class Livro:
    def __init__(self, titulo: str, autor: str, genero: str, disponivel=True):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.disponivel = disponivel

    def __str__(self):
        return f"Titulo: {self.titulo} \nAutor: {self.autor} \nGenero: {self.genero}"

class Usuario:
    def __init__(self, nome: str):
        self.id = str(uuid.uuid4())
        self.nome = nome

    def __str__(self):
        return f"ID: {self.id} \nNome: {self.nome}"

class Emprestimo:
    def __init__(self, nome_livro: str, nome_usuario: str, id_usuario: str, data_emprestimo: datetime, data_devolucao: datetime):
        self.nome_livro = nome_livro
        self.nome_usuario = nome_usuario
        self.id_usuario = id_usuario
        self.data_emprestimo = data_emprestimo
        self.data_devolucao = data_devolucao

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

##############################################################################################################################################################

# HUB DE OPÇÕES DO SISTEMA

def exibir_menu():
    print("\n========== MENU ==========")
    print("1. Cadastrar usuário")
    print("2. Listar usuários")
    print("3. Cadastrar livro")
    print("4. Listar livros")
    print("5. Realizar empréstimo")
    print("6. Devolver livro")
    print("7. Remover livro")
    print("8. Atualizar livro")
    print("9. Calcular multa")
    print("0. Sair")
    print("=======================")

def main():
    biblioteca = Biblioteca()
    
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome_usuario = input("Nome do usuário: ")
            biblioteca.cadastrar_usuario(nome_usuario)
        elif opcao == "2":
            biblioteca.listar_usuarios()
        elif opcao == "3":
            titulo = input("Título do livro: ")
            autor = input("Autor do livro: ")
            genero = input("Gênero do livro: ")
            biblioteca.cadastrar_livro(titulo, autor, genero)
        elif opcao == "4":
            biblioteca.listar_livros()
        elif opcao == "5":
            nome_livro = input("Nome do livro: ")
            nome_usuario = input("Nome do usuário: ")
            try:
                biblioteca.realizar_emprestimo(nome_livro, nome_usuario)
                print(f'Empréstimo do livro "{nome_livro}" para [{nome_usuario}] realizado com sucesso.')
            except Exception as e:
                print(f"Erro: {e}")
        elif opcao == "6":
            nome_livro = input("Nome do livro a ser devolvido: ")
            biblioteca.devolucao(nome_livro)
        elif opcao == "7":
            titulo = input("Título do livro a ser removido: ")
            biblioteca.remover_livro(titulo)
        elif opcao == "8":
            titulo = input("Título do livro a ser atualizado: ")
            novo_titulo = input("Novo título (ou ENTER para manter): ")
            novo_autor = input("Novo autor (ou ENTER para manter): ")
            novo_genero = input("Novo gênero (ou ENTER para manter): ")
            biblioteca.atualizar_livro(titulo, novo_titulo if novo_titulo else None, novo_autor if novo_autor else None, novo_genero if novo_genero else None)
        elif opcao == "9":
            biblioteca.multa()
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
