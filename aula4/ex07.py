
cpf = input('Digite o cpf: ')

with open('registro.txt') as f :
    conteudo = f.readline()


#111.222.333-45;Renato;36;
#111.222.33-46;Carol;31  
for registro in conteudo:
    if cpf in registro.split(':'):
        print(registro)    






exit()
nome =input('Digite seu nome: ')
idade =input('Digite sua idade:')
cpf = input('Digite seu cpf:')

registro = '\n'+ nome + '\n' + idade + '\n'+cpf + ';'
with open ('registro.txt', 'w+') as f:
    f.write(registro)
