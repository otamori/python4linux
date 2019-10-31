#carrinho de compra

#passo1:dicionario de preços

frutas = {'Banana':1.50, 'Morango':3.99, 'Melancia':4.00}
carrinho = []

while True:
    opcao =  int(input( 'Escolha a fruta :\n1- Banana \n2- Morango \n3 - Melancia \n'))
    
    if opcao == 1:
        carrinho.append('Banana')
    elif opcao == 2:
        carrinho.append('Morango')
    elif opcao == 3 :
        carrinho.append('Melancia') 
    elif opcao == 4:
        break 
        
 #passo 3 consolidar preços
 # carrinho = ["Banana", "Banana","Melancia"] 
 
 
soma = 0
 
for fruta in carrinho:
     soma = soma + frutas[fruta]
     
print('Os itens comprados são:')
print(carrinho)
print('O total de compras foi de : R$ ', soma)           
