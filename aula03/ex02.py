frutas = {'banana':1.50, 'morango':3.99, 'melancia':5.00}
cesta = []


while True:
    
    fruta =  (input( 'Que fruta deseja comprar:\n banana:1.50 \n morango:3.99 \n melancia:5.00 \n'))
    if fruta == "banana" :
        cesta.append(frutas["banana"])
    elif fruta == "morango":
        cesta.append(frutas["morango"])
    elif fruta == "melancia":
        cesta.append(frutas["melancia"])
    elif fruta == "4":
        print('Sair')
        break
    else:
        print ('Opção invalida')
soma = 0
for s in cesta:
    soma= soma + s
        

print ("Total da sua compra é: ", soma,"R$")       
