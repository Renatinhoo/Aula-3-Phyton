#Quiz

print("Seja bem vindo ao Quiz!! Tente responder corretamente as perguntas!")

while True:
    escolha1 = int(input("Qual desses animais é conhecido por ser o mais preguiçoso? 1-Macaco 2-Bixo Preguiça 3-Baleia"))


    match escolha1:
        case 1:
            print("Você errou!")
            continue
        case 2:
            print("Você acertou!")
            break
        case 3:
            print("Você errou")
            continue

while True:
    escolha1 = int(input("Qual o meu nome? 1-Carlos 2-Camila 3-Renatinho"))


    match escolha1:
        case 1:
            print("Você errou!")
            continue
        case 2:
            print("Você errou!")
            continue
        case 3:
            print("Você acertou")
            break

while True:
    escolha1 = int(input("Qual o resultado de 1012341234777774741 /  127361623333333  1-2 2-1 3-4"))


    match escolha1:
        case 1:
            print("Você acertou")
            break
        case 2:
            print("Você errou!")
            continue
        case 3:
            print("Você errou!")
            continue

print("Parabens você ganhou!")
