use sucos;

select * from tbcliente where idade = 22;
select * from tbcliente where idade > 22;
select * from tbcliente where idade < 22;
select * from tbcliente where idade <= 22;
select * from tbcliente where idade != '22';

select * from tbcliente where nome >= 'F';
select * from tbcliente where nome like 'F%';
select * from tbproduto where preco_lista between 16.007 and 16.009;
select * from tabela_de_vendedores where percentual_comissao > 0.1;