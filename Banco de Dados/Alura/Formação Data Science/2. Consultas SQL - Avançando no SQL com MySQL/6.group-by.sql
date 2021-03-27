use sucos_vendas;

select*from tabela_de_clientes;

select estado, limite_de_credito from tabela_de_clientes;

select estado, sum(limite_de_credito) from tabela_de_clientes
group by estado;

select embalagem, preco_de_lista from tabela_de_produtos;

select embalagem, max(preco_de_lista) from tabela_de_produtos
group by embalagem;

select embalagem, count(preco_de_lista) from tabela_de_produtos
group by embalagem;

select bairro, sum(limite_de_credito) from tabela_de_clientes
where cidade = 'Rio de Janeiro'
group by bairro;

select estado, bairro, sum(limite_de_credito) from tabela_de_clientes
where cidade = 'Rio de Janeiro'
group by estado, bairro
order by bairro;

select codigo_do_produto, count(quantidade) from itens_notas_fiscais
where codigo_do_produto = '1101035' and quantidade = (select max(quantidade) from itens_notas_fiscais)
group by codigo_do_produto;

