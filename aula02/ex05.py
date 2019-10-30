#Cria uma lista de 15 numeros e apresentara soma deles


#list.append(num)

lista = []
for numero in range(0,4):
    lista.append(int(input('Digite um Numero:')))
    
soma = 0

for numero in lista:
    soma += numero
    
print(lista)





exit()
lista = [15,13,55,10]

soma = 0

for numero in lista:
    soma = soma + numero
    
    print (soma)
