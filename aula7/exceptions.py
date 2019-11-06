
while True:

    try:
    
        opcao = int(input('Escolha a opção: '))
    except Exception as err:
        print("Digite apenas Números")    

    finally:
        print('Sempre executarei esse bloco')
        
    try:
        with open ('arquivoinexistente.txt') as f
            conteudo = f.read()
    except FileNotFoundError as err:
        print ('arquivo não encontrado')
        
     try:
         n1 = 5
         n2 = 0
         
     except Exception as err :
         print (err)               
            
