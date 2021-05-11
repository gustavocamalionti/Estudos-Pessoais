use sucos;

alter table tbcliente
add primary key (cpf);

alter table tbcliente
add column (data_nascimento date);

describe tbcliente;

insert into tbcliente (cpf, nome, endereco1, endereco2, bairro, cidade, estado, cep, idade, sexo, limite_credito, volume_compra, primeira_compra, data_nascimento)
values ('00388934505', 'João da Silva', 'Rua projetada A número 10', '', 'Vila Roman', 'CARATINGA', 'Amazonas', '2222222', 30, 'm', 10000.00, 2000, 0, '1989-10-05');

select*from tbcliente;

alter table tabela_de_vendedores
add column data_admissao date, add column de_ferias bit(1);

describe tabela_de_vendedores;
select * from tabela_de_vendedores;

alter table tabela_de_vendedores
add primary key (matricula);

insert into tabela_de_vendedores (matricula, nome, percentual_comissao, data_admissao, de_ferias) 
values ('00237', 'Roberta Martins', 0.11, '2017-03-18', 1),
('00238', 'Péricles Alves', 0.11, '2016-08-21', 0);

update tabela_de_vendedores
set nome = 'Márcio Almeida da Silva', data_admissao = '2014-08-15', de_ferias = 0
where matricula = '00235';

update tabela_de_vendedores
set data_admissao = '2013-09-17', de_ferias = 1
where matricula = '00236';