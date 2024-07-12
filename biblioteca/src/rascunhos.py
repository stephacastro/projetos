
from datetime import datetime as dt

teste = dt.now()

print(teste)


'''
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

import uuid

id_usuario = uuid.uuid1()
usuario = input('Usuário: ')
tipo = input('Tipo: ')

lista_usuario = [usuario.usuario.lower() for usuario in self.usuario] # type:ignore

if lista_usuario.lower() not in usuario:
    novo_usuario = dict(id_usuario, usuario, tipo)
    self.usuario.append(novo_usuario)
    print(f'Usuário "{novo_usuario}" cadastrado com sucesso.')
else:
    print(f'{usuario} já cadastrado.')'''
