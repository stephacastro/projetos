from datetime import datetime
import uuid

# atributos do livro
class Livros:
    def __init__(self, titulo:str, autor:str, genero:str):
        self.titulo = titulo 
        self.autor = autor
        self.genero = genero
        self.disponivel = True

    # informações dos livros adicionados 
    def __str__(self):
        return f'Titulo: {self.titulo} \n Autor: {self.autor} \n Genero: {self.genero}'

# armazenar os livros e criar uma correlação entre livros e usuarios 
class Biblioteca:
    def __init__(self):
        self.biblioteca = []
           
    def cadastrar_livro(self):
        titulo = input('Titulo: ')
        autor = input('Autor: ')
        genero = input('genero: ')

        titulos = [livro.titulo.lower() for livro in self.biblioteca]

        if titulo.lower() not in titulos:
            novo_livro = dict(titulo, autor, genero)
            self.biblioteca.append(novo_livro)
            print(f'{titulo} adicionado com sucesso!')
        else:
            print('Livro já cadastrado na base de dados')
            
    def listar_livros(self):
        if not self.biblioteca:
            print('Nenhum livro cadastrado.')
            return
        for livro in self.biblioteca:
            print(livro)

    def remover_livro(self):
        remover_titulo = input('Qual o título do livro a ser remover: ')
        for livro in self.biblioteca:
            if livro.titulo.lower() == remover_titulo.lower():
                self.biblioteca.remove(livro)
                print(f'Livro {remover_titulo} removido com sucesso.')
                return
        print('Livro não encontrado.')        

    def atualizar_livro(self):
        atualizar_livro = input('Qual o titulo do livro a ser atualizado: ')
        for livro in self.biblioteca:
            if livro.titulo.lower() == atualizar_livro:
                novo_titulo = input('Novo título ou ENTER para manter.')
                novo_autor = input('Novo autor ou ENTER para manter.')
                novo_genero = input('Novo gênero ou ENTER para manter.')

                if novo_titulo:
                    livro.titulo = novo_titulo
                if novo_autor:
                    livro.autor = novo_autor
                if novo_genero:
                    livro.genero = novo_genero

                print(f'Livro {atualizar_livro} atualizado com sucesso.')
                return
        print('Livro não encontrado.') 

class Usuario:
    def __init__(self):
        self.usuario = []
    
    def __str__(self):
        return f'ID: {self.id} \n Nome: {self.usuario} \n Tipo: {self.tipo}'

    def cadastro(self):
        id_usuario = uuid.uuid1()
        usuario = input('Usuário: ')
        tipo = input('Tipo (LEITOR OU BIBLIOTECÁRIO): ')

        lista_usuario = [usuario.usuario.lower() for usuario in self.usuario]

        if lista_usuario.lower() not in usuario:
            novo_usuario = dict(id_usuario, usuario, tipo)
            self.usuario.append(novo_usuario)
            print(f'Usuário "{novo_usuario}" cadastrado com sucesso.')
        else:
            print(f'{usuario} já cadastrado.')

    def distincao(self):
        raise NotImplemented('Função precisa ser construida')
    
    def listar_usuarios(self):
        if not self.usuario:
            print('Nenhum Usuário cadastrado.')
            return
        for usuario in self.usuario:
            print(usuario)



class Leitor(Usuario):
    def __init__(self, id:int, nome:str):
        #super().__init__(id, nome, tipo='Leitor')
        pass

    def cadastro(self):
        raise NotImplemented('Função precisa ser construida')

    def distincao(self):
        raise NotImplemented('Função precisa ser construida')


class Bibliotecario(Usuario):
    def __init__(self, id:int, nome:str):
        #super().__init__(id, nome, tipo='Bibliotecário')
        pass

    def cadastro(self):
        raise NotImplemented('Função precisa ser construida')

    def distincao(self):
        raise NotImplemented('Função precisa ser construida')


# associar entre livros e usuários 
class Emprestimo:
    def __init__(self, livro, usuario):
        self.livro = livro
        self.usuario = usuario
        #self.data_emprestimo = None
        #self.data_devolucao = None

    def emprestimo(self):
        if self.livro.disponivel:
            self.livro.disponivel = False
            # implementar a hora 
            print(f'Livro "{self.livro.titulo}" emprestado para {self.usuario.usuario}.')
        else:
            print(f'Livro "{self.livro.titulo}" não está disponível.')

    def multa(self):
        raise NotImplemented('Função precisa ser construida')

    def devolucao(self):
        if not self.livro.disponivel:
            self.livro.disponivel = True
            # definir data da devolucao 
            print(f'Livro "{self.livro.titulo}" devolvido por {self.usuario.usuario}.')
        else:
            print(f'Livro "{self.livro.titulo}" já está disponível.')
