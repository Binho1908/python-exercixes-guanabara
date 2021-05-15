print('-----Conversor de Moedas-----')
reais = float(input('Dígite quantos reais você tem: R$ '))
dolar = reais/5.27
yen = reais * 21.75
won = reais * 213.69
euro =  reais/6.40
print(f'{reais:.2f}R$ equivale a \n{dolar:.2f} Dolar(s).\n{yen:.2f}yen(s).\n{won:.2f}won(s) coreano.\n{euro:.2f}euro(s).')
print('cotação do dia 15/05/2021')