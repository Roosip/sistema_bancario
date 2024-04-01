# Definição do menu de opções
menu = '''
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>: '''

# Inicialização das variáveis de conta
saldo = 0
limite = 500
extrato = ""  # Inicializa uma string vazia para armazenar as transações do extrato
numero_sques = 0
LIMITE_SQUES = 3  # Define o limite de saques diários

# Loop principal do programa
while True:
    # Solicitação da opção ao usuário
    opcao = input(menu)

    # Opção de depósito
    if opcao == "d":
        # Solicita o valor do depósito ao usuário
        valor_deposito = float(input("Por favor, digite o valor a ser depositado: "))

        # Verifica se o valor é válido
        if valor_deposito > 0:
            # Atualiza o saldo, adiciona a transação ao extrato e exibe o saldo atualizado
            saldo += valor_deposito
            extrato += f"Depósito de R${valor_deposito:.2f}\n"
            print(f"Seu saldo atualizado é de: R${saldo:.2f}")
        else:
            print("Valor inválido, refaça a ação novamente.")

    # Opção de saque
    elif opcao == "s":
        if numero_sques < LIMITE_SQUES:
            # Verifica se o limite de saques diários ainda não foi atingido
            print("Saque")
            # Solicita o valor do saque ao usuário
            valor_saque = float(input("Digite o valor do saque: "))

            # Verifica se o valor de saque é válido em relação ao limite e saldo disponível
            if valor_saque > limite:
                print(f"O valor do saque é maior que o limite atual de R${limite:.2f}, por favor, insira um valor menor ou igual a R${limite:.2f}.")
            elif valor_saque > 0:
                if saldo - valor_saque >= 0:
                    # Atualiza o saldo, número de saques e limite de saque, adiciona a transação ao extrato e exibe mensagem de sucesso
                    saldo -= valor_saque
                    numero_sques += 1
                    limite -= valor_saque
                    extrato += f"Saque de R${valor_saque:.2f}\n"
                    print(f"Seu saque de R${valor_saque:.2f} foi realizado com sucesso! Seu saldo atual é: R${saldo:.2f}, seu número de saques é de: {numero_sques} de {LIMITE_SQUES} saques e seu limite diário é de: R${limite:.2f}.")
                else:
                    print(f"Não foi possível realizar a transação, pois o saldo é insuficiente. Seu saldo atual é: R${saldo:.2f}")
            else:
                print("Valor de saque inválido.")
        else:
            print("Você atingiu seu limite de saques, volte outro dia.")

    # Opção de extrato
    elif opcao == "e":
        # Exibe o extrato bancário com informações sobre as transações, saldo e limites
        print("\n>>>>>>>>>>>>>>> EXTRATO <<<<<<<<<<<<<<<")
        if extrato:
            print(f"\n>>>>> Aqui está o seu extrato bancário <<<<< \n{extrato} \nSeu saldo é de: R${saldo:.2f} \nSeu Limite de saque diário é de: R${limite:.2f} \nSeu números de saques é de: {numero_sques} saques \nSeu limite de saques é de: {LIMITE_SQUES} saques")
        else:
            print("Não foram realizadas movimentações.")

    # Opção de sair do programa
    elif opcao == "q":
        break

    # Opção inválida
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
