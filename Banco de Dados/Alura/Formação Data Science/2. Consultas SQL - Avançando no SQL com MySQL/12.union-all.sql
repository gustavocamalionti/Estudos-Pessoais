use sucos_vendas; 

select distinct bairro from tabela_de_clientes;
select distinct bairro from tabela_de_vendedores;

select distinct bairro from tabela_de_clientes;
select distinct bairro from tabela_de_vendedores;

/*O union simples junta os registros e faz o distinct*/
select distinct bairro from tabela_de_clientes 
union 
select distinct bairro from tabela_de_vendedores;

select distinct bairro, nome, 'Cliente' as TIPO from tabela_de_clientes 
union 
select distinct bairro, nome, 'Vendedor' as TIPO from tabela_de_vendedores;

select distinct bairro, nome, 'Cliente' as TIPO_CLIENTE from tabela_de_clientes 
union 
select distinct bairro, nome, 'Vendedor' as TIPO_VENDEDOR from tabela_de_vendedores;

select distinct bairro, nome, 'Cliente' as TIPO_CLIENTE, cpf from tabela_de_clientes 
union 
select distinct bairro, nome, 'Vendedor' as TIPO_VENDEDOR, matricula from tabela_de_vendedores;

/*Não aplica o distinct sobre o resultado final da consulta*/
select distinct bairro from tabela_de_clientes
union all
select distinct bairro from tabela_de_vendedores;

/*APLICANDO "FULL JOIN"*/
select tabela_de_vendedores.bairro as BAIRRO_VENDEDORES,
tabela_de_vendedores.nome as NOME_VENDEDORES, 
de_ferias,
tabela_de_clientes.BAIRRO as BAIRRO_CLIENTES, 
tabela_de_clientes.nome as NOME_CLIENTES
from tabela_de_vendedores left join tabela_de_clientes 
on tabela_de_vendedores.BAIRRO = tabela_de_clientes.BAIRRO
union
select tabela_de_vendedores.bairro as BAIRRO_VENDEDORES,
tabela_de_vendedores.nome as NOME_VENDEDORES, 
de_ferias,
tabela_de_clientes.BAIRRO as BAIRRO_CLIENTES, 
tabela_de_clientes.nome as NOME_CLIENTES
from tabela_de_vendedores right join tabela_de_clientes 
on tabela_de_vendedores.BAIRRO = tabela_de_clientes.BAIRRO;
