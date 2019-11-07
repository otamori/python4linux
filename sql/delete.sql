-- DELETE

use 4linux;

SELECT * FROM pessoa;

DELETE FROM pessoa
WHERE nacionalidade_pessoa = 'Nigeriana';

SELECT * FROM pessoa;
