select estado, sum(limite_de_credito) as Soma_limite from tabela_de_clientes
group by estado;

select estado, sum(limite_de_credito) as Soma_limite from tabela_de_clientes
group by estado
having sum(limite_de_credito) > 900000;

select embalagem, max(preco_de_lista) as Maior_preco, min(preco_de_lista) as Menor_Preco from tabela_de_produtos
group by embalagem
having sum(preco_de_lista) <= 80 and max(preco_de_Lista) > 5;


select cpf, count(data_venda) from notas_fiscais
where year(data_venda) = 2016
group by cpf
having count(data_venda) > 2000; 