use sucos_vendas;

select * from tabela_de_vendedores;
select * from notas_fiscais;

select * from tabela_de_vendedores as v inner join notas_fiscais as f
on v.matricula = f.matricula;

select a.matricula, a.nome, count(*) from tabela_de_vendedores as a inner join notas_fiscais as b
on a.matricula = b.matricula
group by a.matricula, a.nome;

select * from notas_fiscais order by numero;
select * from itens_notas_fiscais order by numero;
select * from tabela_de_produtos;

/*Obtenha o faturamento anual da empresa. Leve em consideração que o valor financeiro das vendas consiste em multiplicar a quantidade pelo preço.*/
select 
year(a.data_venda) as Período_Anual, 
round(sum(b.quantidade*b.preco),2) as faturamento
from notas_fiscais as a 
inner join itens_notas_fiscais as b on a.numero = b.numero
group by year(a.data_venda)
order by year(a.data_venda);

/*incorporando um case when após resultado de query*/
select x.periodo_anual, x.faturamento,
case
    when x.faturamento > 40000000 then 'ACIMA DO ESPERADO'
    when x.faturamento < 40000000 then 'ABAIXO DO ESPERADO'
    else 'VALOR ESPERADO'
end as media 
from
(select 
year(a.data_venda) as periodo_anual, 
round(sum(b.quantidade*b.preco),2) as faturamento
from notas_fiscais as a 
inner join itens_notas_fiscais as b on a.numero = b.numero
group by year(a.data_venda)
order by year(a.data_venda)) as x
group by x.periodo_anual;
