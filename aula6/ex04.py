#criar uma classe de conta Bancaria
# Ela devera conter os seguintes atributos:
## agencia
## conta
## titular
## saldo


# Os comportamentos esperados de uma conta são
## Saque <-  Validar se tem dinheiro
## Deposito
## Ver saldo


# 1 Criar uma classe
# class <Nomde da classe>
# 2 criar construtor
# def __init__(self):
# self.atributos =
# 3 criar os metodos
# def nomedo Metodo(self, atributos ...):

# 1 Criar uma classe
class Conta():
    # 2 criar construtor
    def __init__(self,agencia=0,conta=0,titular='',saldo=0):
        self.agencia = agencia
        self.conta = conta
        self.titular = titular
        self.__saldo = saldo
        
        
    def saque(self,valor):
        if self.__saldo < valor:
            print('Saldo Insuficiente')
        else:
            self.__saldo -= valor
            return self.__saldo
            
    def deposito(self,valor):
        if valor < 0:
            print('Não foi possivel completar a operação')
        else:
            self.__saldo += valor
            return self.__saldo
            
    def verSaldo(self):
        return self.__saldo
        
    def setSaldo(self,valor):
        self.__saldo += valor    
        
    def transferencia (self, valor, conta):
        if valor > self.__saldo:
            return 'Saldo insuficiente'
        else:
            self.__saldo -= valor
            conta.setSaldo(valor)    
            
#instancia novo objeto do tipo de Conta        
conta = Conta(4300,34115, 'Renato')   
conta2 = Conta(2222,8888,'Maria')

#realiza o deposito                                 
print(conta.deposito(500))

print (conta.saque(150))
#realizar a transferencia
conta.transferencia(150,conta2)
print ('Valor da transferencia é: ',conta2.verSaldo(),'R$')
