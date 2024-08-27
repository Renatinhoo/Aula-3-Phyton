num1 = float(input("Digite o primeiro número da conta:"))
num2 = float(input("Digite o segundo número da conta:"))



while True:
    escolha = int(input("Escolha uma das operações Disponiveis: 1-Soma/2-Subtração/3-Multiplicação/4-Divisão"))



    match escolha:
        case 1:
            conta = num1 + num2
            break
        case 2:
            conta = num1 - num2
            break
        case 3:
            conta = num1 * num2
            break
        case 4:
            conta = num1 / num2
            break
        case _:
            print("Operação Inválida, Digite um número dentro dos parâmetros exibidos!")
            continue

print(f"O resultado da sua conta é: {conta}")
