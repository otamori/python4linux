# Funções e Variaveisdo modelo

#1 passo


carrinho = []

#2 passo criar funcao para adicionar itens

def adiciona_item(valor):
    carrinho.append(valor)
    
def total_carrinho(lista_compra):
    soma = 0
    for item in lista_compra:
        soma += item
    return soma        

