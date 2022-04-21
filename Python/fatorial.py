numero = int(input('Digite um número: '))
fact = 1
if numero == 1:
    numero = 0
else:
    while numero >= 1:
        print(numero)
        fact = fact*numero
        print(fact)
        numero = numero - 1
print(fact)
