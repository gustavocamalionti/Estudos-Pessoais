use sucos_vendas;

select * from tabela_de_vendedores;
select * from tabela_de_clientes;

select count(*) from tabela_de_clientes;

select 
tabela_de_vendedores.bairro,
tabela_de_vendedores.nome, 
de_ferias,  /*Não há a necessidade de especificar a tabela pois o campo "de_ferias" só existe na tabela de vendedores*/
tabela_de_clientes.BAIRRO, 
tabela_de_clientes.nome 
from tabela_de_vendedores inner join tabela_de_clientes 
on tabela_de_vendedores.BAIRRO = tabela_de_clientes.BAIRRO;

/*verificar se existe algum vendedor que possui seu escritório em um local onde não há clientes*/
select 
tabela_de_vendedores.bairro as BAIRRO_VENDEDORES,
tabela_de_vendedores.nome as NOME_VENDEDORES, 
de_ferias,
tabela_de_clientes.BAIRRO as BAIRRO_CLIENTES, 
tabela_de_clientes.nome as NOME_CLIENTES
from tabela_de_vendedores left join tabela_de_clientes 
on tabela_de_vendedores.BAIRRO = tabela_de_clientes.BAIRRO;

/*Verificar se há escritório no bairro de um cliente*/
select 
tabela_de_vendedores.bairro as BAIRRO_VENDEDORES,
tabela_de_vendedores.nome as NOME_VENDEDORES, 
de_ferias,  
tabela_de_clientes.BAIRRO as BAIRRO_CLIENTES, 
tabela_de_clientes.nome as NOME_CLIENTES
from tabela_de_vendedores right join tabela_de_clientes 
on tabela_de_vendedores.BAIRRO = tabela_de_clientes.BAIRRO;

/*verificar as duas condições simultaeamente - ESSE COMANDO NÃO EXISTE NO MYSQL, MOTIVO PELO QUAL DÁ ERRO*/
/*RESOLUÇÃO ALTERNATIVA COM FULL JOIN NO ARQUIVO 12*/
select 
tabela_de_vendedores.bairro as BAIRRO_VENDEDORES,
tabela_de_vendedores.nome as NOME_VENDEDORES, 
de_ferias,  
tabela_de_clientes.BAIRRO as BAIRRO_CLIENTES, 
tabela_de_clientes.nome as NOME_CLIENTES
from tabela_de_vendedores full join tabela_de_clientes 
on tabela_de_vendedores.BAIRRO = tabela_de_clientes.BAIRRO;

/*analise combinatória entre bairros de vendedores e bairros de clientes*/
select 
tabela_de_vendedores.bairro as BAIRRO_VENDEDORES,
tabela_de_vendedores.nome as NOME_VENDEDORES, 
de_ferias,  
tabela_de_clientes.BAIRRO as BAIRRO_CLIENTES, 
tabela_de_clientes.nome as NOME_CLIENTES
from tabela_de_vendedores cross join tabela_de_clientes; /*from tabela_de_vendedores, tabela_de_clientes; >>>>>TAMBÉM FUNCIONA<<<<<< /*
 
