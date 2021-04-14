use sucos_vendas;

select * from tabela_de_produtos;

select nome_do_produto, preco_de_lista,
case
	when PRECO_DE_LISTA >= '12' then 'PRODUTO CARO'
    when (PRECO_DE_LISTA >= '7' and PRECO_DE_LISTA < '12') then 'PRODUTO EM CONTA'
    else 'PRODUTO BARATO'
end as 'Classificacao_De_Preco'
from tabela_de_produtos
order by Classificacao_De_Preco;

select embalagem,
case
	when preco_de_lista >= 12 then 'PRODUTO CARO'
	when preco_de_Lista >=7 and preco_de_Lista < 12 then 'PRODUTO EM CONTA'
	else 'PRODUTO BARATO' 
end as STATUS_PRECO, avg(preco_de_lista) as PRECO_MEDIO
from tabela_de_produtos
group by embalagem,
case 
	when preco_de_lista >= 12 then 'PRODUTO CARO'
	when preco_de_lista >= 7 and preco_de_Lista < 12 then 'PRODUTO EM CONTA'
	else 'PRODUTO BARATO'
end
order by embalagem;

select nome, data_de_nascimento,
case
	when year(data_de_nascimento) < 1990 then 'Velho' 
    when year(data_de_nascimento) > 1995 then 'Criança'
    else 'Jovem'
end as classificacao
from tabela_de_clientes;

