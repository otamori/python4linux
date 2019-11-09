#List Comprehension
from functools import reduce

lista = [0,1,2,3,4,5,6,7,8,9,10]

nova_lista = [x for x in lista if x %2 !=0]
print (lista)
print (nova_lista)

#funções Anonimas

print('Funcoes Anonimas')

quadrado = lambda x: x**2

print(quadrado(2))

##filter

print('filter')

multiplo_2 = lambda x: x%2 == 0

nova_lista = list(filter(multiplo_2,lista))
print(nova_lista)

## MAP

print('Map')

nova_lista = list(map(lambda x: x*2,lista))
print(nova_lista)

##REDUCE
print('Reduce')
lista = [1,1,1,1,1]
total = reduce(lambda x,y: x+y, lista)
print(total)

#(((((+1)+1)+1)+1)
