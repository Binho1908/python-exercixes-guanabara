# Exercício Python 015: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

kilomPer = float(input('Quantidade de Km percorrida pelo carro alugado? '))
dias = float(input('Quantidade de dias alugado'))
custoKmRodado = float(0.15)
custoAluguelDia = float(60)

custoKilomTotal = kilomPer * custoKmRodado
custoAluguelTotal = dias * custoAluguelDia
custoTotal = custoKilomTotal + custoAluguelTotal
print(f'O valor a pagar é {custoTotal}')