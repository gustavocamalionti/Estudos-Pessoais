/*EXERCICIO 01: Uma coluna com os sabores, depois o ano que 
eu estou analisando, que é 2016, e eu quero olhar isso de forma ordenada do maior 
para o menor vendidos em quantidade, sem considerar tamanhos diferentes, e no 
final um percentual de participação.*/

use sucos_vendas;
select * from notas_fiscais;
select * from itens_notas_fiscais;
select * from tabela_de_produtos;

/*TABELA: VENDA_SABOR - MONTANDO A LÓGICA*/
select 
c.SABOR, year(a.DATA_VENDA) as Ano, sum(b.QUANTIDADE) as Quantidade
from notas_fiscais as a 
	inner join 
    itens_notas_fiscais as b on a.numero = b.numero
	inner join tabela_de_produtos as c on b.codigo_do_produto = c.codigo_do_produto
where year(a.data_venda) = 2016
group by c.SABOR
order by sum(b.QUANTIDADE) desc, c.sabor asc; 

/*TABELA: VENDA TOTAL - DESCOBRINDO A QUANTIDADE TOTAL DE VENDAS NO ANO DE 2016*/
select 
year(a.data_venda) as ano, sum(b.QUANTIDADE) as quantidade
from notas_fiscais as a 
inner join itens_notas_fiscais as b on a.numero = b.numero
inner join tabela_de_produtos as c on b.codigo_do_produto = c.codigo_do_produto
where year(a.data_venda) = 2016;

/*NOMEANDO E JUNTANDO AS TABELAS:VENDA_SABOR e VENDA_TOTAL*/
select 
	* from (select 
	c.SABOR, year(a.DATA_VENDA) as Ano, sum(b.QUANTIDADE) as Quantidade, c.TAMANHO
	from notas_fiscais as a 
		inner join 
		itens_notas_fiscais as b on a.numero = b.numero
		inner join tabela_de_produtos as c on b.codigo_do_produto = c.codigo_do_produto
	where year(a.data_venda) = 2016
	group by c.SABOR
	order by sum(b.QUANTIDADE) desc, c.sabor asc) as VENDA_SABOR
inner join
	(select 
	year(a.data_venda) as ano, sum(b.QUANTIDADE) as quantidade
	from notas_fiscais as a 
	inner join itens_notas_fiscais as b on a.numero = b.numero
	inner join tabela_de_produtos as c on b.codigo_do_produto = c.codigo_do_produto
	where year(a.data_venda) = 2016) as VENDA_TOTAL 
    on VENDA_SABOR.ano = VENDA_TOTAL.ano;
    
    /*RELATÓRIO FINAL*/
select 
venda_sabor.sabor, venda_sabor.ano, venda_sabor.quantidade, round(venda_sabor.quantidade/venda_total.quantidade_total*100,2) as participação 
from (select 
	c.SABOR, year(a.DATA_VENDA) as Ano, sum(b.QUANTIDADE) as Quantidade, c.TAMANHO
	from notas_fiscais as a 
		inner join 
		itens_notas_fiscais as b on a.numero = b.numero
		inner join tabela_de_produtos as c on b.codigo_do_produto = c.codigo_do_produto
	where year(a.data_venda) = 2016
	group by c.SABOR
	order by sum(b.QUANTIDADE) desc, c.sabor asc) as VENDA_SABOR
inner join
	(select 
	year(a.data_venda) as ano, sum(b.QUANTIDADE) as quantidade_total
	from notas_fiscais as a 
	inner join itens_notas_fiscais as b on a.numero = b.numero
	inner join tabela_de_produtos as c on b.codigo_do_produto = c.codigo_do_produto
	where year(a.data_venda) = 2016) as VENDA_TOTAL 
    on VENDA_SABOR.ano = VENDA_TOTAL.ano;
    
/*EXERCICIO 02:Modifique o relatório mas agora para ver o ranking das vendas por tamanho, sem considerar o sabor.*/
select venda_sabor.ano, venda_sabor.quantidade, venda_sabor.tamanho, round(venda_sabor.quantidade/venda_total.quantidade_total*100,2) as participação 
from (select 
	c.SABOR, year(a.DATA_VENDA) as Ano, sum(b.QUANTIDADE) as Quantidade, c.TAMANHO
	from notas_fiscais as a 
		inner join 
		itens_notas_fiscais as b on a.numero = b.numero
		inner join tabela_de_produtos as c on b.codigo_do_produto = c.codigo_do_produto
	where year(a.data_venda) = 2016
	group by c.tamanho
	order by sum(b.QUANTIDADE) desc, c.sabor asc) as VENDA_SABOR
inner join
	(select 
	year(a.data_venda) as ano, sum(b.QUANTIDADE) as quantidade_total
	from notas_fiscais as a 
	inner join itens_notas_fiscais as b on a.numero = b.numero
	inner join tabela_de_produtos as c on b.codigo_do_produto = c.codigo_do_produto
	where year(a.data_venda) = 2016) as VENDA_TOTAL 
    on VENDA_SABOR.ano = VENDA_TOTAL.ano;
    
    /*DESCOBRINDO TODOS OS CASOS DE TAMANHO*/
    select distinct tamanho from tabela_de_produtos;
    
    /*brincando com case when
	case
		when c.TAMANHO = '2 Litros' then 2000
		when c.TAMANHO = '1,5 Litros' then 1500
		when c.TAMANHO = '1 Litro' then 1000
		when c.TAMANHO = '700 ml' then 700
		when c.TAMANHO = '470 ml' then 470
		when c.TAMANHO = '350 ml' then 350
		else c.TAMANHO = 'edit'
	end as tamanho_em_ml */
    
    
