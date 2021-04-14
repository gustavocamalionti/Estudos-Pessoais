use sucos_vendas;

select distinct bairro from tabela_de_vendedores;

select * from tabela_de_clientes where bairro in ('Tijuca','Jardins','Copacabana','Santo Amaro');
select * from tabela_de_clientes where bairro in (select distinct bairro from tabela_de_vendedores);

select embalagem, max(preco_de_lista) from tabela_de_produtos
group by embalagem;

/*CHAMANDO A SELECAO DE X*/
select X.embalagem, X.preco_maximo from 
(select embalagem, max(preco_de_lista) as preco_maximo from tabela_de_produtos
group by embalagem) as X
where x.preco_maximo >= 10;

/*Qual seria a consulta usando subconsulta que seria equivalente a:*/
SELECT CPF, COUNT(*) FROM notas_fiscais
WHERE YEAR(DATA_VENDA) = 2016
GROUP BY CPF
having COUNT(*) > 2000;

select X.CPF, X.contador from 
(select CPF, COUNT(*) as contador FROM notas_fiscais
WHERE YEAR(data_venda) = 2016
group by CPF) as X
where X.contador > 2000;


