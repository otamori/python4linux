

class Onibus():
    
    def __init__(self):
        self.capacidade = 0
        self.origem = '177h2b'
        self.destino = '3445HB'
        self.velocidade = 0
    
    def acelerar(self):
        self.velocidade += 20   

    def frear(self):
        if self.velocidade == 0:
            print('Onibus parado')
        else:
            self.velocidade -=20
            
    def embarque(self, num_pessoas):
        if self.capacidade == 45 - num_pessoas:
            print("Onibus cheio")
        else:
            self.capacidade += num_pessoas
             
             
    def desembarque(self, num_pessoas):
        if self.capacidade == 0:
            print('Onibus vazio')
        else:
            self.capacidade -= num_pessoas

onibus = Onibus()
onibus.acelerar()

print(onibus.velocidade)

onibus.frear()
print(onibus.velocidade)

onibus.embarque(2)
onibus.desembarque(1)

print(onibus.capacidade)
onibus.desembarque(1)              
              
print(onibus.capacidade)                        
onibus.desembarque(1)
