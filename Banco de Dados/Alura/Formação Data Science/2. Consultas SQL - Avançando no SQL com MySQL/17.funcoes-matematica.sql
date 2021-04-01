use sucos_vendas;

select (23+((25-2)/2)*45) as Resultado;

select ceiling(23.342133) as resultado; /*Maior inteiro acima do número*/
select round(23.340329) as resultado; /*arredondamento mais coerente*/ 
select floor(23.34329) as resultado; /*Arredondamento para um inteiro abaixo do número*/
select rand() as resultado; /*Número aleatório*/

select 
	numero, quantidade, preco, round(quantidade*preco, 2) as faturamento 
from itens_notas_fiscais;

/*Na tabela de notas fiscais temos o valor do imposto. Já na tabela de itens temos a quantidade 
e o faturamento. Calcule o valor do imposto pago no ano de 2016 arredondando para o menor inteiro.*/

select * from notas_fiscais;
select * from itens_notas_fiscais;

select floor(sum(a.imposto*(b.quantidade*b.preco))) as SOMA_IMPOSTOS_2016
from notas_fiscais as a 
inner join itens_notas_fiscais as b on a.numero = b.numero
where year(a.data_venda) = 2016
group by year(a.data_venda);


