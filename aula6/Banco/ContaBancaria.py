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
            
