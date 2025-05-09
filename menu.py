texto = input("Digite uma frase:")
opcao = -1
while opcao != 5:
    print('1) Converta a frase para maiúscula')
    print('2) Converta a frase para minúscula')
    print('3) Substitua a letra a pela letra o')
    print('4) Conte quantas vogais tem a frase')
    print('5) Sair')
    opcao = int(input("Escolha: "))

    if opcao == 1:
        print(frase.upper())
    elif opcao == 2:
        print(frase.lower())
    elif opcao == 3:
        print(frase.replace('a', 'o'))
    elif opcao == 4:
        print("Fazer")