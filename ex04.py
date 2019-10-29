

n1 = int (input ( 'Digite um valor: '))
n2 = int (input ( 'Digite um valor:  '))
ope = input ( 'Qual operação deseja fazer?\n add,\n sub,\n div,\n multi:\n ')


if ( ope == 'add'):
    print('A soma dos valores são : {} + {} = {}'.format(n1,n2,n1 + n2))
    
if ( ope == 'sub'):
    print ('A subtração dos valores é: {} - {} = {}'.format (n1,n2, n1 - n2))
    
if ( ope == 'div'):
    print ('A divisão dos valores é: {} / {} = {}'.format (n1,n2, n1 / n2))    
    
if ( ope == 'multi'):
    print ('A multiplicação dos valores é: {} * {} = {}'.format (n1,n2, n1 * n2))    
