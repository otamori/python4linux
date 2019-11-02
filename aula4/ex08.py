    dic = { 'CPF':'',
             'NOME':'',
             'EMAIL':'',
             'UF':''
                 
           }  
def main():
    
    while True:
        opcao =  int(input( 'Sistema de cadastro :\n1- Cadastrar pessoa \n2- Consultar \n3 - Sair \n'))
        if opcao == 1:
             cadastrar()
        elif opcao == 2:
             consultar()
        elif opcao == 3 :
              break

def cadastrar():
    cpf = input('Digite o seu cpf sem ponto:\n')
    nome = input('Digite o seu nome:\n')
    email = input('Digite seu email:\n')
    uf = input('Digite seu estado:\n')

    registrar = '\n' +cpf +';' + nome +';'+ email +';'+ uf 

    print(registrar)

    with open('registro.txt', 'a') as f :
        f.write(registrar)

def consultar():
    
    with open('registro.txt', 'r') as f:
        conteudo = f.readlines()
        print(conteudo)


if __name__ == '__main__':   
    main()
