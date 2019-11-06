from ContaBancaria import Conta


def criarConta(carteira):
    print('Informe os dados:')
    
    
    agencia= input('Agencia: ')
    conta = input('Conta:')
    titular = input('Titular: ')
    saldo = 0
    
    
    carteira[titular] = Conta(agencia, conta, titular, saldo)
    

def consultarSaldo(carteira):
    conta = input('Informe o numero da conta: ')
    
    for elemento in carteira.values():
        if elemento.getConta() == conta:
            print(elemento.verSaldo())
            break
            
    else:
        print('Conta não cadastrada')  
        
        
def realizarSaque(carteira):
    conta = input('Informe o numero da conta: ')
    valor = input('Informe valor para saque: ')
    
    for elemento in carteira.values():
        if elemento.getConta() == conta:
            print(elemento.saque(valor))
            break
            
    else:
        print('Conta não cadastrada')
        
        
def efetuarDeposito(carteira):
    
    conta = input('Informe o numero da conta: ')
    valor = input('Informe valor para Deposito:')
    for elemento in carteira.values():
       if elemento.getConta() == conta:
           print(elemento.deposito(valor))
           break

    else:
        print('Conta não cadastrada')
        
def efetuarTransferencia(carteira):
    if len(carteira) < 2:
        print('Número insuficiente de contas cadastradas')
    else:
    conta = input('Informe o numero da conta: ')
    valor = float
        
