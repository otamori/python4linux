frutas = ['banana', 'morango','melancia']
cesta = []



while True:
    fruta = int (input( 'Digite a sua fruta : \n 1 - banana \n 2 - morango \n 3 - melancia \n'))
    if fruta == 1 :
        cesta.append(frutas[0])
    elif fruta == 2:
        cesta.append(frutas[1])
    elif fruta == 3:
        cesta.append(frutas[2])
    elif fruta == 4:
        print('Sair')
        break
    else:
        print ('Opção invalida')
print(cesta)

                       
