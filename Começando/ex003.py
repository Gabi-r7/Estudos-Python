def option():
    opcao = int(input('1 - Adição;\n2 - Subtração;\n3 - Multiplicação;\n4 - Divisão;\n5 - Sair;\n Digite sua escolha: '))
    if opcao == 5:
        print('Volte sempre!')
        quit
    elif opcao == 1:
        adicao()
    elif opcao == 2:
        subtracao()
    elif opcao == 3:
        multiplicacao()
    elif opcao == 4:
        divisao()
    else:
        print('Opção inválida. Tente novamente.\n')
        option()

def adicao():
    print(f'O resultado da adição entre {n1} e {n2} é {n1+n2}\n')
    option()

def subtracao():
    print(f'O resultado da subtração entre {n1} e {n2} é {n1-n2}\n')
    option()

def multiplicacao():
    print(f'O resultado da multiplicação entre {n1} e {n2} é {n1*n2}\n')
    option()

def divisao():
    print(f'O resultado da divisão entre {n1} e {n2} é {n1/n2}\n')
    option()

print('\nCalculadora!\n')
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
option()