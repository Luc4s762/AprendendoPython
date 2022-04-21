from datetime import date
data_atual = date.today()
print('Hoje é: ',data_atual)
print('O ano é: ',data_atual.year)
Nascimento = int(input('Digite sua data de nascimento: '))
Ano = int(data_atual.year)
idade = Ano - Nascimento
print('Você têm: ', idade,' anos')
if idade >= 18:
    print('Você é maior de idade')
elif idade < 18:
    print('Você é menor de idade')
