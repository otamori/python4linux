#Aproveitando a classe do ex04
# Criar uma interface para:
## 1)Criar contas
##2) Realizar operações Bancárias:
#2.1 Consultar Saldo
#2.2 Realizar Saque
#2.3 Efetuar Deposito
#2.4 Fazer Transferencia
from ex04 import *


    def 
            
    while True:
        print ('Sistema de Cadastro')
        opcao = input('Escolha a opcao:\n1 - Criar contas\n2- Realizar Operações\n2.1 - Consultar Saldo\n2.2 - Realizar Saque\n2.3 Efetuar Deposito\n2.4 - Fazer Transferência\n3- Sair\n')
        
        if opcao == '1':
            cadastro()
        elif opcao == '2':
            consulta()
        elif opcao == '3' :
             break
        else:
            print('Opção Invalida')
