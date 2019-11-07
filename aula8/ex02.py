from BancoDeDados import *

bd = ConexaoBanco()
bd.iniciaConexao()

SQL = 'SELECT * FROM pessoa'

registros = bd.executaSQL(SQL)

for linha in registros:
            print ('--------------------------')
            print ('ID: ', linha['id_pessoa'])
            print ('Nome: ', linha['nome_pessoa'])
            print ('Nacionalidade: ', linha['nacionalidade_pessoa'])
            print ('Idade: ', linha['idade_pessoa'])
            
bd.terminaConexao()
