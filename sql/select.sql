-- Consulta

-- passo 0 : escolher o banco de dados

use 4linux;

SELECT * FROM pessoa;

SELECT * FROM pessoa
WHERE nacionalidade_pessoa = 'Brasileira';

SELECT * FROM pessoa
WHERE idade_pessoa > 25;


SELECT * FROM pessoa
WHERE nome_pessoa like "Phi%";
