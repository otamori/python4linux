#classes

class Carro():
    #construtor
    def __init__(self, modelo='', cor='', velocidade=0, ano=0):
        self.modelo = modelo
        self.cor = cor
        self.velocidade = velocidade
        self.ano = ano

    def acelerar(self):
        self.velocidade += 10
        
    def frear(self):
        if self.velocidade == 0:
            print('O carro esta parado')
        else:
            self.velocidade -= 10   
        
    
        
#criei um objeto


fusca = Carro('Fusca', 'Vermelho', 0, 1975)
brasilia = Carro('Brasilia', 'Amarela', 0, 1985)
verona = Carro()
print(fusca.modelo)
print(fusca.cor)
print(fusca.velocidade)

fusca.acelerar()
fusca.acelerar()
print(fusca.velocidade)        
