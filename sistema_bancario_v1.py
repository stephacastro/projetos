saldo = 0
limite = 500
numero_saque = 0
LIMITE_SAQUES = 3
transacoes = []

menu = """
    [0] - Depositar
    [1] - Sacar
    [2] - Extrato 
    [3] - Sair 
=> """

while True:
    opcao = input(menu)

    if opcao == '0':
        print('Digite o valor a ser Depositado:')
        valor = int(input())
        print('Depósito realizado com sucesso!')
        transacoes.append(('Depósito', valor))
        saldo += valor
    
    elif opcao == '1':
        if numero_saque < LIMITE_SAQUES:
            print('Digite o valor para Saque:')
            saque = int(input())
            if saque <= saldo:
                transacoes.append(('Saque', saque))
                saldo -= saque
                numero_saque += 1   
                print('Saque realizado com sucesso!')
            else:
                print('Saldo insuficiente para saque!')
        else:
            print('Você excedeu o limite diário de saque!')
    
    elif opcao == '2':
        print('\nExtrato:')
        for tipo, valor in transacoes:
            print(f'{tipo}: R$ {valor}')
        print(f'Saldo Atual: R$ {saldo}\n')
    
    elif opcao == '3':
        break
    
    else:
        print('Opção inválida, selecione uma operação existente!')

