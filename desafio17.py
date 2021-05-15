import math
catetoAdjacente = float(input('Dígite o cateto adjacente: '))
catetoOposto = float(input('Dígite o cateto oposto: '))
catetoOp = catetoOposto * catetoOposto
catetoAd = catetoAdjacente * catetoAdjacente
catetoTot = catetoOp + catetoAd
hipotenusa = math.sqrt(catetoTot)

print(f'Dado {catetoAdjacente} Cateto adjacente, {catetoOposto} Cateto oposto, a hipotenusa é igual a {hipotenusa}')
