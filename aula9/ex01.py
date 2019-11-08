#mongo

from pymongo import MongoClient

client = MongoClient()

bd = client.pessoa

# INSERT

bd.pessoa.insert_many(
    [
        {
            'nome':'Bill Gates',
            'nacionalidade':'Americano',   
            'idade': 65 ,
          
    

    },
     {
            'nome':'Steve jobs',
            'nacionalidade':'Americano',   
            'idade': 62 ,
          
    

    },
    
      {
            'nome':'Wozniack',
            'nacionalidade':'Americano',   
            'idade': 72 ,
          
    

    }


    ]
)
