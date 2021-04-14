/*Operador distinct irá separar apenas as combinações que não irão se repetir*/

select embalagem, tamanho from tabela_de_produtos;
select embalagem, tamanho from tabela_de_produtos where sabor = 'Laranja';
select distinct embalagem from tabela_de_produtos;

select distinct bairro from tabela_de_clientes 
where cidade = 'Rio de Janeiro';

/*Usando Limit*/
select * from tabela_de_produtos limit 5;
select * from tabela_de_produtos limit 2,3;
select * from tabela_de_produtos limit 0,2;

select * from notas_fiscais where data_venda = '2017-01-01';
select * from notas_fiscais where data_venda = '2017-01-01' limit 10;