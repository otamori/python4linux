#Utilizar o exercicio da cesta de compras
#e criar funçoes para :
#1 - adicionar item na lista
#2 - somar os items de uma listallfolders
#3 - apresentar o resultado     



def main():
    opcao =  int(input( 'Escolha a fruta :\n1- Banana \n2- Morango \n3 - Melancia \n'))    

def adiciona(lista):
    
    while True:
 
        if opcao == 1:
            lista.append('Banana')
        elif opcao == 2:
            lista.append('Morango')
        elif opcao == 3 :
            lista.append('Melancia') 
        elif opcao == 4:
            break 
        return lista
        
        
#def soma(lista):

#resultado = 0

    
    



#def resultado(lista)



    
        
if __name__ == '__main__':   
    main()
