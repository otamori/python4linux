#passo 1importar o modulo da cesta

from lib.cesta import *

def main():
    dic = {'Banana': 1.50, 'Morango': 3.99, 'Melancia': 4.00}
    
    while True:
        
        opcao = input('Escolha a fruta: \n1 - Banana\n2- Morango\n3 - Melancia\n')
        if opcao == '1':
            adiciona_item(dic ['Banana'])
        elif opcao == '2':
            lista.append(dic ['Morango'])
        elif opcao == '3' :
            lista.append(dic ['Melancia']) 
        elif opcao == '4':
            break 
        else:
            print (' Opcao invalida')
            
            print (total_carrinho(carrinho)) 
            
            
if __name__ == '__main__':   
    main()
            
