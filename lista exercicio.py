# Exercicio 1

print('Eu me chamo Allan\nTenho 24 anos\nMoro na Bahia')

# # Exercicio 2

nome = input('Digite o seu nome: ')
print('Olá, {}!'.format(nome))


# # Exercicio 3

altura = float(input('Digite a atura do retângulo: '))
base = float(input('Digite a base do retângulo: '))

area = altura * base
print(f'A área do retângulo mede: {area:.2f}m²')



# # Exercicio 4

import locale

locale.setlocale(locale.LC_ALL, 'pt_br')

pastel = 8
refrigerante = 5

qt_pastel = float(input('Quantos pasteis vc deseja? '))
qt_refri = float(input('Quantos refrigerantes vc deseja? '))

total = (pastel * qt_pastel) + (refrigerante * qt_refri)
total_reais = locale.currency(total, grouping=True)
print(f'O total do seu pedido é  {total_reais}')


# # Exercicio 5

import locale

locale.setlocale(locale.LC_ALL, 'pt_br')

salario = float(input('Digite o seu salário'))
aumento = salario * 0.05
salario_novo = salario + aumento
bonus = (salario_novo * 0.2)
ano = (salario_novo * 12) + bonus

aumento_reais = locale.currency(aumento, grouping=True)
salario_novo_reais = locale.currency(salario_novo, grouping=True)
bonus_reais = locale.currency(bonus, grouping=True)
ano_reais = locale.currency(ano, grouping=True)
print(f'Seu novo salário é de: {salario_novo_reais}')
print(f'O seu bônus é de: {bonus_reais}')
print(f'Você receberá {ano_reais} anual')


# # Exercicio 6

base_menor = float(input('Digite a base menor do trapézio: '))
base_maior = float(input('Digite a base maior do trapézio: '))
altura = float(input('Digite a altura do trapézio: '))

area = ((base_maior + base_menor) * altura) / 2

print(f'A área do trapézio mede {area:.2f}m²')


# # Exercicio 7

import locale

locale.setlocale(locale.LC_ALL, "pt_br")

valor = float(input('Digite o valor que deseja investir: '))

valor_um_ano = valor * 0.06 + valor
valor_dois_anos = valor_um_ano * (1+ 0.06)
valor_tres_anos = valor_dois_anos * (1+ 0.06)
valor_quatro_anos = valor_tres_anos * (1+ 0.06)
valor_cinco_anos = valor_quatro_anos * (1+ 0.06)

print(f'Saldo após 1 ano: {locale.currency(valor_um_ano, grouping=True)}')
print(f'Saldo após 2 anos: {locale.currency(valor_dois_anos, grouping=True)}')
print(f'Salfo após 3 anos: {locale.currency(valor_tres_anos, grouping=True)}')
print(f'Saldo após 4 anos: {locale.currency(valor_quatro_anos, grouping=True)}')
print(f'Saldo após 5 anos: {locale.currency(valor_cinco_anos, grouping=True)}')


# Exercicio 8

import math

dias_uma_caixa = int(20 / 1.6)
caixa_mes = 30 / dias_uma_caixa


qt_meses = int(input('Digite a quantos meses são necessários: '))

qt_caixas = math.ceil(qt_meses * caixa_mes)

print(f'Você deve comprar {qt_caixas} caixas de remédio')


# # Exercicio 9

import math

raio = float(input('Digite o raio do circulo: '))
diametro = raio * raio
area = math.pi * diametro

print(f'A área do circulo mede {area:.2f}m².')


# # Exercicio 10

minuto = 60
hora = 60 * minuto
dia = 24 * hora


dia_dig = int(input('Digite a quantidade de dias: '))
hora_dig = int(input('Digite a quantidade de horas: '))
minuto_dig = int(input('Digite a quantidade de minutos: '))

segundos = (dia_dig * dia) + (hora_dig * hora) + (minuto_dig * minuto)

print(f'Em {dia_dig} dia(s), {hora_dig} hora(s) e {minuto_dig} minuto(s) temos {segundos} segundos')

# Exercicio 11

minutos = 60
hora = minutos * 60
dia = hora * 24

segundo_dig = int(input('Digite a quantidade de segundos: '))

dia_total = segundo_dig // dia
resto_segundo = segundo_dig % dia

hora_total = resto_segundo // hora
resto_segundo = resto_segundo % hora

minuto_total = resto_segundo // minutos
resto_segundo = resto_segundo % minutos

print(
    ( f'{segundo_dig} segundo(s) equivale(m) a {dia_total} dia(s),'
      f'{hora_total} hora(s), {minuto_total} minuto(s) e {resto_segundo} segundo(s).'))


# Exercicio 12

Celsius = float(input('Insira a temperatura em Celsius :'))
Fahrenheit = (Celsius * 9 / 5) + 32
Kelvin = Celsius + 273.15

print(f'{Celsius:.2f}º Celsius equivale a {Fahrenheit:.2f}º Fahrenheit e {Kelvin:.2f}º Kelvin')
