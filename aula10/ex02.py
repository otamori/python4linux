#apis

import requests


cep = input('Digite o CEP:')
for c in cep:
    return cep

#https://viacep.com.br/ws/06223040/json

destino = 'https://viacep.com.br/ws/'+cep+'/json'
          
          
          
resposta = requests.get(destino)

if resposta.status_code == 200:
    json = resposta.json()
    print ('CEP:', json['cep'])
    print ('Logradouro:', json['logradouro'])
    print ('Bairro:', json['bairro'])
    print ('UF', json['uf'])
    print ('IBGE', json['ibge'])
    print ('GIA', json['gia'])
 
