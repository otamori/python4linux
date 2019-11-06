 
import unittest
from ex01 import Onibus

class testeFuncoes(unittest.TestCase):
    
    def test_construtor(self):
        o = Onibus()
        self.assertEqual(0,o.capacidade)
        self.assertEqual('177h2b',o.origem)
        self.assertEqual('3445HB',o.destino)
        self.assertEqual(0,o.velocidade)
    
    def test_acelerar(self):
        o = Onibus()
        o.acelerar()
        self.assertEqual(20,o.velocidade)
        
    def test_frear(self):
        o = Onibus()
        o.frear()
        self.assertEqual(0,o.velocidade)

        

        
        
if __name__=='__main__':
    unittest.main()
