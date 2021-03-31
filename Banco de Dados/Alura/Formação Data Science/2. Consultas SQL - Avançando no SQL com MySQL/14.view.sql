use sucos_vendas;

select embalagem, max(preco_de_lista) as maior_preco from tabela_de_produtos
group by embalagem;

select x.embalagem, x.maior_preco from
(select embalagem, max(preco_de_lista) as maior_preco from tabela_de_produtos
group by embalagem) as x 
where x.maior_preco >= 10;

drop view vw_maiores_embalagens; 

create or replace view VW_maiores_embalagens as (select embalagem, max(preco_de_lista) as maior_preco from tabela_de_produtos
group by embalagem);

select 
a.embalagem, a.maior_preco 
from VW_maiores_embalagens as a
where a.maior_preco >= 10;

select a.nome_do_produto, a.preco_de_lista, b.maior_preco,
-1*(a.preco_de_lista/b.maior_preco) * 100 as percentual
from tabela_de_produtos as a 
inner join VW_maiores_embalagens as b
on a.embalagem = b.embalagem;