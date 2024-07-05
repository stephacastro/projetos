# atributos do livro
class Livros:
    def __init__(self, titulo:str, autor:str, genero:str):
        self.titulo = titulo 
        self.autor = autor
        self.genero = genero
        self.disponivel = True

    # informações dos livros adicionados 
    def __str__(self):
        raise NotImplemented('Função precisa ser construida')

# armazenar os livros e criar uma correlação entre livros e usuarios 
class Biblioteca:
    def __init__(self):
        self.biblioteca = []
           
    def cadastrar_livro(self):
        titulo = input('Titulo: ')
        autor = input('Autor: ')
        genero = input('genero: ')

        lista = [] 

        titulos = [item['titulo'].lower() for item in lista]

        if titulo.lower() not in titulos:
            dicionario = dict(titulo=titulo, autor=autor)
            lista.append(dicionario)
            print(f'{titulo} adicionado com sucesso!')
        else:
            print('Livro já cadastrado na base de dados')
            print(lista)

    def listar_livros(self):
        return "Livros Cadastrados\n".join(livro for livro in lista)

    def remover_livro(self):
        raise NotImplemented('Função precisa ser construida')

    def atualizar_livro(self):
        raise NotImplemented('Função precisa ser construida')

class Usuario:
    def __init__(self, id:int, usuario:str, tipo:str):
        self.id = id 
        self.usuario = usuario
        self.tipo = tipo

    def cadastro(self):
        raise NotImplemented('Função precisa ser construida')

    def distincao(self):
        raise NotImplemented('Função precisa ser construida')
    
    def listar_usuarios(self):
        raise NotImplemented('Função precisa ser construida')


class Leitor(Usuario):
    def __init__(self, id:int, nome:str):
        super().__init__(id, nome, tipo='Leitor')

    def cadastro(self):
        raise NotImplemented('Função precisa ser construida')

    def distincao(self):
        raise NotImplemented('Função precisa ser construida')


class Bibliotecario(Usuario):
    def __init__(self, id:int, nome:str):
        super().__init__(id, nome, tipo='Bibliotecário')

    def cadastro(self):
        raise NotImplemented('Função precisa ser construida')

    def distincao(self):
        raise NotImplemented('Função precisa ser construida')


# associar entre livros e usuários 
class Emprestimo:
    def __init__(self):
        #super().__init__(titulo, autor, genero, isbn_id)
        raise NotImplemented('Função precisa ser construida')

    def emprestimo(self):
        raise NotImplemented('Função precisa ser construida')

    def multa(self):
        raise NotImplemented('Função precisa ser construida')

    def devolucao(self):
        raise NotImplemented('Função precisa ser construida')
