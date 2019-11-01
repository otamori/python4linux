def soma (* numeros):
    resultado = 0
    for num in numeros:
        resultado += num
        
    return resultado
     
     
     
def main():
#   numeros = [1,2,3,4,5] 
    print(soma(2,4,6,8))
 
if __name__ == '__main__':   
    main()
