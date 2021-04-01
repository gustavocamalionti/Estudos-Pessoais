/*pedido que o gerente da área de vendas da empresa de suco de frutas, 
ele quer que eu faça um relatório mostrando dentro de todas as vendas, 
quais delas foram validas e quais foram invalidas.*/

use sucos_vendas;

select * from notas_fiscais;
select * from itens_notas_fiscais;
select * from tabela_de_clientes;

select 
a.cpf, a.data_venda, b.quantidade 
from notas_fiscais as a 
inner join itens_notas_fiscais as b on a.numero = b.numero;

/*Consulta com vendas de clientes por mês*/
select 
a.cpf, date_format(a.data_venda, '%Y-%m') as Ano_mes, sum(b.quantidade) as quantidade_vendas
from notas_fiscais as a 
inner join itens_notas_fiscais as b on a.numero = b.numero
group by a.cpf, date_format(a.data_venda, '%Y-%m')
order by a.cpf, (date_format(a.data_venda, '%Y-%m'));

/*Limite de compra por clientes*/
select * from tabela_de_clientes;
select c.cpf, c.nome, c.volume_de_compra as quantidade_limite from tabela_de_clientes as c;

/*Consulta com vendas de clientes por mês*/
select 
a.cpf, c.nome, date_format(a.data_venda, '%Y-%m') as Ano_mes, sum(b.quantidade) as quantidade_vendas, c.volume_de_compra as quantidade_limite,
case
	when sum(b.quantidade) > c.volume_de_compra then 'Inválido'
    else 'Válido'
end as Status
from notas_fiscais as a 
inner join itens_notas_fiscais as b on a.numero = b.numero
inner join tabela_de_clientes as c on a.cpf = c.cpf
group by a.cpf, c.nome, date_format(a.data_venda, '%Y-%m')
order by a.cpf, c.nome, (date_format(a.data_venda, '%Y-%m'));

/*Nesta aula construímos um relatório que apresentou os clientes que tiveram vendas inválidas. 
Complemente este relatório listando somente os que tiveram vendas inválidas e calculando a 
diferença entre o limite de venda máximo e o realizado, em percentuais.*/

select 
a.cpf, c.nome, date_format(a.data_venda, '%Y-%m') as Ano_mes, sum(b.quantidade) as quantidade_vendas, c.volume_de_compra as quantidade_limite,
case
	when sum(b.quantidade) > c.volume_de_compra then 'Inválido'
    else 'Válido'
end as status, ((sum(b.quantidade))/(c.volume_de_compra)-1)*100 as Porcentagem_Ultrapassada
from notas_fiscais as a 
inner join itens_notas_fiscais as b on a.numero = b.numero
inner join tabela_de_clientes as c on a.cpf = c.cpf
group by a.cpf, c.nome, date_format(a.data_venda, '%Y-%m')
having Status = 'Inválido'
order by a.cpf, c.nome, (date_format(a.data_venda, '%Y-%m'));


