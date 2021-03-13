create database cadastro;
use cadastro;
create table pessoas (
nome varchar(30),
idade tinyint(3),
sexo char(1),
endereço varchar(100),
nacionalidade varchar(100)
);

describe pessoas;