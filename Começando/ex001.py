#Escreva um programa que calcule a soma dos números pares de 1 a N, onde N é um número fornecido pelo usuário.

n = 1
soma = 0
nDigitado = int(input('Digite um número: '))

while n != nDigitado:
    if n % 2 == 0:
        soma += n
    n += 1
print(f'A soma é de {soma}!')