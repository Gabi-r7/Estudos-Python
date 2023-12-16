#Crie uma função que verifica se uma palavra fornecida pelo usuário é um palíndromo (lê-se igual de trás para frente).
palavra = input('Digite uma palavra: ')
Tpalavra = len(palavra)

palavra2 = palavra[::-1]

if palavra == palavra2:
    print(f'A palavra "{palavra}" é um palíndromo.')
else:
    print(f'A palavra "{palavra}" não é um palíndromo.')