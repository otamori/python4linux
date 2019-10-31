dicionario = {'nota1':5.5, 'nota2':7.5,'nota3':4.5}

soma = 0

for elemento in dicionario.values():
    soma=soma+elemento

media = soma /len(dicionario)

print(media)
