saldo = 0
opcao = 1
saque_diario = 0
registros_depositos = []
registros_saques = []
indice_deposito = 0
indice_saque = 0

while opcao != 0:
    opcao = int(input(
    '''
    ************Bem-Vindo************

    Qual operação deseja realizar:

    1 - Depósito
    2 - Saque
    3 - Extrato  
    0 - Encerrar Operação 

    *********************************
'''))
    
    #DEPÓSITO
    if opcao == 1:
        valor_deposito = float(input("Qual o valor do depósito: R$"))
        if valor_deposito > 0:
            saldo += valor_deposito
            print(f"Seu depósito foi realizado com sucesso.")
            registros_depositos.append(valor_deposito)
            print(registros_depositos)
        else:
            print("valor inválido para depósito")

    #SAQUE
    elif opcao == 2:
        if saque_diario < 3:
            valor_saque = float(input("Qual é o valor que Deseja sacar: R$"))
            if valor_saque <= 500:
                if saldo >= valor_saque:
                    print("Saque realizado com sucesso.")
                    saque_diario += 1
                    saldo = saldo - valor_saque
                    registros_saques.append(valor_saque)
                else:
                    print("Saldo insuficiente")
            else:
                print("Seu limite de saque é de R$500,00.")
        else: 
            print("Operação não realizada. Limite de saque diário atingido")

    #EXTRATO
    elif opcao == 3:
        numero_elementos_depositos = len(registros_depositos)
        numero_elementos_saques = len(registros_saques)
        print('''           Extrato Bancário \n''')
        while indice_deposito < numero_elementos_depositos:
            print(f'''      Depósito___________R${registros_depositos[indice_deposito]:.2f}''')
            indice_deposito += 1
        while indice_saque < numero_elementos_saques:
            print(f'''      Saques_____________R${registros_saques[indice_saque]:.2f}''')
            indice_saque += 1
        print(f'''      Saldo______________R${saldo:.2f}''')

    #OPÇÃO INVÁLIDA
    else:
        print("Opção inválida escolha uma opção válida para prosseguir.\n")
print("\nOperação finalizada")