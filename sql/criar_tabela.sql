-- Passo0: Ver os bancos de dados

show databases;

-- Passo1: Selecionar o Banco de Dados

use 4linux;

-- Passo2: Criar a Tabela

CREATE TABLE pessoa(
    id_pessoa int not null auto_increment,
    nome_pessoa varchar(50) not null,
    nacionalidade_pessoa varchar(20) not null,
    idade_pessoa int not null,
    PRIMARY KEY (id_pessoa)
);
