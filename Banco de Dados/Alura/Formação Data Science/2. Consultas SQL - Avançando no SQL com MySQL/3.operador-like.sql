use sucos_vendas;

select * from tabela_de_produtos where sabor like '%Maçã%';
select * from tabela_de_produtos where sabor like '%Cereja%' and Embalagem = 'PET';

select count(*) from tabela_de_clientes where nome like '%Mattos';

