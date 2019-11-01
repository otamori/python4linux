# Arquivos
with open('arquivo.txt', 'r') as f:
    conteudo = f.read()
    
    
print(conteudo)
print(type(conteudo))


conteudo += '\nRenato ;36;111.111.222-33'

with open ('arquivo2.txt', 'w+') as f :
    f.write(conteudo)
    
