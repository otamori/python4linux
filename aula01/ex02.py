# exercicio de media

#entrada de dados
num1 = float (input ('Digite o primeiro número:'))
num2 = float (input ('Digite o segundo número:'))
num3 = float (input ('Digite o terceiro número: '))
#calculo da média
resultado = (num1 + num2 + num3) /3
#apresentação do resultado
#print ( "A média do valor é {0:.2f}".format( resultado)) 
print ( "A média das notas {0:.2f},{0:.2f},{0:.2f} = {0:.2f}".format(num1,num2,num3,resultado))
