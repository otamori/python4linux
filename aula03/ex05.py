


def soma(num1, num2):
    resultado_soma = num1 + num2
    return resultado_soma
    
def  sub(num1,num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2
    
def main():
    x = int(input('Digite o primeiro valor: '))
    y = int(input('Digite o segundo valor: '))
    
    
    resultado_soma= soma(x,y)
    print(resultado_soma)
    resultado_sub = sub(x,y)
    print(resultado_sub)
    resultado_divide= divide(x,y)
    print (resultado_divide)
    resultado_multiply= multiply(x,y) 
    print (resultado_multiply)
    
if __name__ == '__main__':
    main()
