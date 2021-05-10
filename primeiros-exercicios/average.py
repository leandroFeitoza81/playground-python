import random

""" Calcula a média aritmética dos valores contidos em uma lista. """
contador = 1
lista = []
soma = 0


while contador <= 10:
    """Este laço irá gerar uma lista de 10 numeros aleatórios entre 1 e 99"""
    numero_randomico = random.randint(1, 99)
    lista.append(numero_randomico)
    contador += 1

for numero in lista:
    """Soma todos numeros na lista"""
    soma += numero

""" Printa na tela a média aritmética 👇"""
print("A média dos números na lista é:", soma / 10)
