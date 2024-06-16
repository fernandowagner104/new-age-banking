# Código do Desafio: Criando um sistema bancário.

menu = """
Seja bem vinda(o) ao New Age Banking! O seu banco do futuro!
Por gentileza, informe a operação:
[1] - DEPÓSITO
[2] - SAQUE
[3] - EXTRATO
[4] - SAIR
"""

balance = 0
number_of_withdrawl = 0
WITHDRAWL_DAILY = 3
limit = 500
extract = ""

while True:
    option = int(input(menu))

    if option == 1:
        deposit_value_daily = float(input("Informe o valor a ser depositado:"))

        while deposit_value_daily <= 0.0:
            print("Você precisa inserir um valor maior que zero!")
            deposit_value_daily = float(input("Informe o valor a ser depositado:"))
            balance += deposit_value_daily

        balance += deposit_value_daily
        extract += f"Você Depositou: R${deposit_value_daily:.2f}\n"
        print(f"O valor R${deposit_value_daily} foi depositado com sucesso!")

    elif option == 2:
        
        if number_of_withdrawl < WITHDRAWL_DAILY:
           withdrawl_value_daily = float(input("Informe o valor a ser sacado:"))

           if balance == 0.0 or balance < withdrawl_value_daily:
               print("Você não tem saldo suficiente para realizar o saque!")
               continue
           
           elif withdrawl_value_daily > limit:
               print("Você ultrapassou o limite de saque!")
               continue
           
           balance -= withdrawl_value_daily
           number_of_withdrawl += 1
           extract += f"Você Sacou: R${withdrawl_value_daily:.2f}\n"
           print(f"O saque de R${withdrawl_value_daily:.2f} foi realizado com sucesso!")
           
        else:
            print("Você excedeu o número de saques por dia!")

    elif option == 3:
        if extract == "":
            print("Não foram realizadas movimentações!")
            continue
        else:
            text_extract = " EXTRATO DA CONTA "
            text_transactions = " MOVIMENTAÇÕES DA CONTA "
            print(text_extract.center(40, "#"))
            print(f"Saldo em conta: R${balance:.2f}\n")
            print(text_transactions.center(40, "#"))
            print(extract)

    elif option == 4:
        break    

