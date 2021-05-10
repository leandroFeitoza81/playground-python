numero = int(input("Digite um número inteiro maior que 1: "))
SYMBOL = "*"
count = 1

if numero <= 1:
    print("Este valor não é valido. Entre um número maior que 1")

while count <= numero:
    print(numero * SYMBOL)
    count += 1
