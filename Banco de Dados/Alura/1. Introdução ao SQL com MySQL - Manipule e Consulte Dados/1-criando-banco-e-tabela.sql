CREATE DATABASE sucos;
USE sucos;
CREATE TABLE tbCliente (
cpf VARCHAR(11),
nome VARCHAR(100),
endereco1 VARCHAR(150),
endereco2 VARCHAR(150),
bairro VARCHAR(50),
cidade VARCHAR(50),
estado VARCHAR(50),
cep VARCHAR(80),
idade SMALLINT,
sexo ENUM('m','f'),
limite_credito FLOAT,
volume_compra FLOAT,
primeira_compra BIT(1));

CREATE TABLE tabela_de_vendedores (
matricula VARCHAR(5),
nome VARCHAR(100),
percentual_comissao float);

drop table tbcliente2;



