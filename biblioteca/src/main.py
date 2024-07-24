from src.models.biblioteca import Biblioteca

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

main()
