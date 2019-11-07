# Exemplo de conexão com o banco de dados

import pymysql.cursors
from env import *

try:
    conexao = pymysql.connect(
        host= 'localhost',
        user = USERNAME,
        password = PASSWORD,
        db='4linux',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
        
        )
        
except Exception as err:
    print('Não foipossivel conectar com o Banco de Dados')
    print(err)
    
    
    
else:
    
    #nome = input('Digite o nome: ')
    #nacionalidade = input ('Digite a nacionalidade:')
    #idade = input ('Digite a idade: ')
    
    with conexao.cursor() as cursor:
        SQL = " SELECT * FROM pessoa"
        #SQL = 'INSERT INTO pessoa (nome_pessoa, nacionalidade_pessoa, idade_pessoa) '
        #SQL += 'VALUES ("{}","{}",{})'.format(nome,nacionalidade,idade)
        
        
        cursor.execute(SQL)
        #salvar as alterações    
        conexao.commit()
        for linha in cursor:
            print ('--------------------------')
            print ('ID: ', linha['id_pessoa'])
            print ('Nome: ', linha['nome_pessoa'])
            print ('Nacionalidade: ', linha['nacionalidade_pessoa'])
            print ('Idade: ', linha['idade_pessoa'])
            
            
finally:
    
    conexao.close()            
