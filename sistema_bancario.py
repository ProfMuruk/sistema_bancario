

print("Bem-vindo ao sistema bancário!")
print("Selecione uma opção: ")

opcoes = ("d = depositar", "s = sacar", "e = extrato", "q = sair")
saldo = 0
quantidade_saques = 0
LIMITE_SAQUES = 3

while True:
    for i in opcoes:
        print(i)

    opcao = input("\n")
    if opcao == "d":
        valor = float(input("Valor do deposito: "))
        if valor > 0:
            saldo += valor

    elif opcao == "s":
        valor = float(input("valor do saque: "))
        if (valor > 0 and valor <= saldo) and (quantidade_saques < LIMITE_SAQUES):
            saldo -= valor
            quantidade_saques += 1
        elif quantidade_saques >= LIMITE_SAQUES:
            print("Você só pode sacar 3 vezes no dia!")
        else:
            print("Valor insuficiente!")
    
    elif opcao == "e":
        print(f"Seu saldo é de: R${saldo:.2f}")

    elif opcao == "q":
        break

    else:
        print("Opção inválida, selecione uma opção da lista")
    