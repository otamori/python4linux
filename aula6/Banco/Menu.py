#Aproveitando a classe do ex04
# Criar uma interface para:
## 1)Criar contas
##2) Realizar operações Bancárias:
#2.1 Consultar Saldo
#2.2 Realizar Saque
#2.3 Efetuar Deposito
#2.4 Fazer Transferencia
import Funcoes import *

def main ():
    
    carteira = {}
    
    while True:
        ops = {
            '1':criarConta,
            '2':consultarSaldo,
            '3':realizarSaque, 
            '4':efetuarDeposito,
            '5':efetuarTransferencia,
            '6':exit     
        
        } 
            
   opcao = input ('Escolha a opção:\n1 - Criar conta\n '+
                    '2 - Consultar Saldo\n3 -Saque\n'+
                    '4 - Deposito\n5 - Transferência\n'+
                    '6 - Sair\n')
                    
                    
   ops[opcao](carteira)
   
if__name__=='__main__':
   main()
