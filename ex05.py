# receber o ano de nascimeto

nasci = int ( input( 'Digite o ano de seu nascimento: '))

if ( nasci <= 1964):
    print( 'Você pertence a geração BBoomer')
elif ( nasci > 1964 and nasci <= 1981):
    print('Você pertence a Geração x')
elif ( nasci >1981 and nasci <= 1996):
    print( 'Você pertence a Geração Y')
else:
    print ( 'Você pertence a Geração Z')
            
