
class Playlist:
    def __init__(self):
        self.playlist = {}

    def cadastrar_musica(self):
        nome_musica = input('Qual o nome da música: ')
        nome_artista = input('Qual o nome do artista: ')

        if nome_artista in self.playlist:
            self.playlist[nome_artista].append(nome_musica)
        else:
            self.playlist[nome_artista] = [nome_musica]

        print(f'Música "{nome_musica}" cadastrada com sucesso 🎵')

    def ver_playlist(self):
        print("\nPlaylist:")
        for artista, musicas in self.playlist.items():
            print(f"Artista: {artista}")
            for musica in musicas:
                print(f"  - {musica}")
        print()

    def deletar_musica(self):
        nome_musica = input('Qual música deseja remover: ')
        for musicas in self.playlist.values():
            if nome_musica in musicas:
                musicas.remove(nome_musica)
                print(f'Música "{nome_musica}" removida com sucesso 🎵')
                return
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

    minha_playlist = Playlist()

    while True:
        escolha = int(input("Sua Escolha: "))

        if escolha == 1:
            print('===================================================')
            minha_playlist.cadastrar_musica()

        elif escolha == 2:
            print('===================================================')
            minha_playlist.ver_playlist()

        elif escolha == 3:
            print('===================================================')
            minha_playlist.deletar_musica()

        elif escolha == 4:
            print('===================================================')
            print('Obrigado por utilizar a minha playlist!')
            break

        else:
            print('===================================================')
            print("Opção inválida. Escolha novamente.")

if __name__ == "__main__":
    main()
