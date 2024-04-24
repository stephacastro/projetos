def cadastrar_musica(playlist):
    nome_musica = input('Qual o nome da música: ')
    playlist.append(nome_musica)
    print(f'Música "{nome_musica}" cadastrada com sucesso 🎵')

def ver_playlist(playlist):
    print("\nPlaylist:")
    for musica in playlist:
        print(musica)
    print()

def deletar_musica(playlist):
    musica_a_remover = input('Qual música deseja remover: ')
    if musica_a_remover in playlist:
        playlist.remove(musica_a_remover)
        print(f'Música "{musica_a_remover}" removida com sucesso 🎵')
    else:
        print("Música não encontrada na playlist.")

def main():
    print(
        """🎵 Playlist Musical 🎵 

        Escolha uma das opções:
        [1] - Cadastrar Nova Música
        [2] - Ver Playlist
        [3] - Remover uma música
        [4] - Sair
        """
    )

    banco_musicas = []

    while True:
        escolha = int(input("Sua Escolha: "))

        if escolha == 1:
            print('===================================================')
            cadastrar_musica(banco_musicas)

        elif escolha == 2:
            print('===================================================')
            ver_playlist(banco_musicas)

        elif escolha == 3:
            print('===================================================')
            deletar_musica(banco_musicas)

        elif escolha == 4:
            print('===================================================')
            print('Obrigado por utilizar a minha playlist!')
            break

        else:
            print('===================================================')
            print("Opção inválida. Escolha novamente.")

if __name__ == "__main__":
    main()
