from utils.choices import pedra, papel, tesoura
from utils.choices import emoji_papel, emoji_pedra, emoji_tesoura, emoji_bolinha_verde, emoji_trofeu, emoji_explosao
from utils.choices import emoji_primeiro_lugar, emoji_triste, emoji_maos_apertando
import random

print(f'\n========================== BEM VINDOS AO {emoji_pedra}  {emoji_papel}   {emoji_tesoura} ==========================\n')

def pedra_papel_tesoura(escolha_usuario, escolha_maquina):
    if escolha_maquina == escolha_usuario:
        return 'Empate'
    elif escolha_maquina == pedra:
        if escolha_usuario == papel:
            return 'Usuário'
        else:
            return 'Máquina'
    elif escolha_maquina == papel:
        if escolha_usuario == tesoura:
            return 'Usuário'
        else:
            return 'Máquina'
    elif escolha_maquina == tesoura:
        if escolha_usuario == pedra:
            return 'Usuário'
        else:
            return 'Máquina'

opcoes = [pedra, papel, tesoura]

vitorias_maquina = 0
vitorias_usuario = 0
empates = 0
contagem = 0

while contagem < 5:
    
    escolha_usuario = int(input("\nQual opção você escolhe? \n[0] Pedra \n[1] Papel\n[2] Tesoura\n"))

    escolha_maquina = random.randint(0, 2)

    print(f'\nEscolha da Usuário: {opcoes[escolha_usuario]}')
    print(f'\nEscolha da Máquina: {opcoes[escolha_maquina]}')

    resultado = pedra_papel_tesoura(opcoes[escolha_usuario], opcoes[escolha_maquina])

    print(f'{resultado} venceu {emoji_bolinha_verde}')

    if resultado == 'Usuário':
        vitorias_usuario += 1
    elif resultado == 'Máquina':
        vitorias_maquina += 1
    else: 
        empates = empates + 1
    
    contagem += 1

print(f'\n========================== PLACAR {emoji_trofeu} ==========================')
print(f'\nUsuário fez {vitorias_usuario} ponto(s) {emoji_explosao}')   
print(f'\nMáquina fez {vitorias_maquina} ponto(s) {emoji_explosao}')
print(f'\nO Jogo empatou {empates} vezes {emoji_maos_apertando}\n')

if vitorias_maquina > vitorias_usuario:
    print(f'\nMáquina venceu o jogo com {vitorias_maquina} ponto(s) {emoji_primeiro_lugar}')
elif vitorias_usuario > vitorias_maquina:
    print(f'\nUsuário venceu o jogo com {vitorias_usuario} ponto(s) {emoji_primeiro_lugar}')
else:
    print(f'O jogo terminou em empate {emoji_triste}')
