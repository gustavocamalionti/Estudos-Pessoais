select * from tabela_de_produtos order by preco_de_lista; /*ascendente(asc) fica subentendido*/
select * from tabela_de_produtos order by preco_de_lista desc; /*decrescente*/

select * from tabela_de_produtos order by nome_do_produto asc;
select * from tabela_de_produtos order by nome_do_produto desc;

select * from tabela_de_produtos order by embalagem, nome_do_produto;
select * from tabela_de_produtos order by embalagem desc, nome_do_produto asc;

select codigo_do_produto from tabela_de_produtos where nome_do_produto = 'Linha Refrescante - 1 Litro - Morango/Limão';
select max(quantidade) from itens_notas_fiscais where codigo_do_produto = '1101035' order by quantidade desc;
