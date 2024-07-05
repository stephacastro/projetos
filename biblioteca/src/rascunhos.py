print('######################################')
titulo = input('Titulo: ')
autor = input('Autor: ')
print('######################################\n')

lista = [{'titulo':'teste', 'autor':'teste'}] 


titulos = [item['titulo'].lower() for item in lista]

if titulo.lower() not in titulos:
    dicionario = dict(titulo=titulo, autor=autor)
    lista.append(dicionario)
    print(f'{titulo} adicionado com sucesso!')
else:
    print('Livro já cadastrado na base de dados')

print('Remover Livro')

if titulo.lower() in titulos:
    print('')


