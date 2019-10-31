#passo1: criar a lista de frutas

frutas = ['banana', 'Morango', 'Melancia']

cesta = list()


while True:
    print ("Escolha a sua fruta")
    print ("1 - banana")
    print ("2 - Morango")
    print ("3 - Melancia")
    
    escolha = int(input("Digite a opção:"))
    
    if escolha == 1:
        cesta.append(frutas[0])
    elif escolha == 2:
        cesta.append(frutas[1])
    elif escolha == 3:
        cesta.append(frutas[2])
    elif escolha == 4:
        break
        
    else:
        print('Opção Inválida')
        
print(cesta)                       
        
