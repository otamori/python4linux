-- Updates

-- Passos 0: escolher o banco de dados

use 4linux;

UPDATE pessoa
SET nome_pessoa = "Joaquim",
    nacionalidade_pessoa = "Portuguesa"
WHERE id_pessoa = 1;    

SELECT * FROM pessoa
WHERE id_pessoa = 1;
