#calculadora com funções

def soma(num1, num2):
    resultado_soma = num1 + num2
    return resultado_soma
    
def  sub(num1,num2):
    return num1 - num2
    
def multi(num1,num2):
    return num * num2
    
def div(num1,num2):
    if num2 == 0:
        print('Não dividirás por zero')
        
     else:
         return num1/num2
         
def main()
    n1 = int(input('N1: '))
    n2 = int(input('N2: '))
    opcao = input('Escolha a opção:\n1 - Soma\n2- Subtração\n3- Multiplicação\n4- Divisão'
    
    if opcao =='1':
        print(soma(n1,n2))
     elif opcao == '2':
         print(sub(n1,n2)
     elif opcao == '3':
         print(multi(n1,n2) 
     elif opcao == '3':
         print(multi(n1,n2)                       
