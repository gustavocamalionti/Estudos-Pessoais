create database if not exists vendas_sucos;
use vendas_sucos;


create database if not exists vendas_sucos2;
drop database if exists vendas_sucos2;

create table if not exists produtos(
	codigo varchar(10) not null,
	descritor varchar(100) null,
	sabor varchar(50) null,
	tamanho varchar(50) null,
	embalagem varchar(50) null,
	preco_lista float null,
	primary key (codigo));

create table if not exists vendedores(
	matricula varchar(5) not null,
	nome varchar(100) null,
	bairro varchar(50) null,
	comissao float null,
	data_adimissao date null, /*Erro de português proposital*/
	ferias bit(1) null,
	primary key (matricula));

/*alterando nome do campo*/
alter table vendedores
change data_adimissao data_admissao date null;

create table if not exists clientes(
	cpf varchar(11) not null,
    nome varchar(100) null,
    endereco varchar(150) null,
    bairro varchar(50) null,
    cidade varchar(50) null,
    estado varchar(50) null,
    cep varchar(8) null,
    data_nascimento date null,
    idade int(2) null,
    sexo enum('M','F') null,
    limite_credito float null,
    volume_compra float null,
    primeira_compra bit(1) null,
    primary key (cpf));

create table if not exists tabela_de_vendas(
numero varchar(5) not null,
data date null,
cpf varchar(11) null,
matricula varchar(5) null,
imposto float null,
primary key (numero));

/*Alterando nome da tabela*/
alter table tabela_de_vendas
rename to itens_notas;