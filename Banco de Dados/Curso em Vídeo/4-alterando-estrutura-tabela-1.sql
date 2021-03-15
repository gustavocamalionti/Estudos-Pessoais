describe pessoas;

/*Alterando a Tabela e adicionando um campo*/
alter table pessoas
add column profissao varchar(10);

/*Removendo uma coluna*/
alter table pessoas
drop column profissao;

/*Adicionando um campo em uma posição específica*/
alter table pessoas
add column profissao varchar(10) after nome;

alter table pessoas
add codigo int first; 

desc pessoas;

/*Modificando o Tipo Primitivo do Campo*/
alter table pessoas
modify column profissao varchar(20);

/* Alterando o nome do campo*/
alter table pessoas
change column profissao prof varchar(20);

/*Alterando o nome da tabela*/
alter table pessoas
rename to gafanhotos;

desc gafanhotos;

select*from pessoas;