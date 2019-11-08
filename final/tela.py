#mongo

from pymongo import MongoClient

client = MongoClient()

bd = client.pessoa

def main ():
    
    carteira = {}
    
    while True:
        ops = {
            '1':criarCadastro,
            '2':consultarCadastro,
            '3':realizarAlteracao, 
            '4':deletarAlteracao,
            '5':exit     
        
        } 
            
opcao = input ('Escolha a opção:\n1 - Criar Cadastro\n '+
                    '2 - Consultar Cadastro\n3 -Realizar Alteração \n'+
                    '4 - Deletar Alteracao\n5 - Sair\n'+
                    '6 - Sair\n')
                    
                    
ops[opcao](carteira)
   
