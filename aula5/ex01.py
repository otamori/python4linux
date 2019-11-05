
dic = { 'CPF':'',
        'NOME':'',
        'EMAIL':'',
        'UF':''
             
        }  

arq = 'cadastro.csv'

def main():
    while True:
        print ('Sistema de Cadastro')
        opcao = input('Escolha a opcao:\n1 - Cadastro\n2- Consulta\n3- Sair\n')
        
        if opcao == '1':
            cadastro()
        elif opcao == '2':
            consulta()
        elif opcao == '3' :
             break
        else:
            print('Opção Invalida')
            
def cadastro():
       dic ['CPF'] = input('CPF: ')
       dic ['NOME'] = input('NOME: ')
       dic ['EMAIL'] = input('EMAIL: ')
       dic ['UF'] = input('UF: ') 
       
        
       registro = '\n' + dic['CPF'] + ';' + dic['NOME'] + ';' + dic['EMAIL'] + ';' + dic['UF']
       with open(arq, 'w') as f:
           f.write(registro)
         
           
def consulta():
    
    dic['CPF'] = input ('Digite o CPF para a busca: ')
    saida = Nome
    with open(arq, 'r') as f:
        registro = f.readlines()
                
                
    for linha in registro:
        if dic['CPF'] in linha.split(';'):
           saida = linha/split(';')
           print('CPF:', saida[0])
           print('NOME:', saida[1])
           print('EMAIL:', saida[2])
           print('UF:', saida[3])
                 
    if saida == Nome:
       print('registro não encontrado')                               
if __name__ == '__main__':   
    main()
