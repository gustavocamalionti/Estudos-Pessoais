use sucos;
describe tabela_de_vendedores;

select * from tbcliente where idade = 22;
select * from tbcliente where idade > 22;
select * from tbcliente where idade < 22;
select * from tbcliente where idade <= 22;
select * from tbcliente where idade != '22';

select * from tbcliente where nome >= 'F';
select * from tbcliente where nome like 'F%';
select * from tbproduto where preco_lista between 16.007 and 16.009;
select * from tabela_de_vendedores where percentual_comissao > 0.1;

select * from tbcliente where data_nascimento = '1995-01-13';
select * from tbcliente where data_nascimento > '1995-01-13';
select * from tbcliente where data_nascimento <= '1995-01-13';
select nome, data_nascimento from tbcliente where year(data_nascimento) between 1980 and 1999;
select nome, data_nascimento from tbcliente where month(data_nascimento) = 10;

select * from tabela_de_vendedores where year(data_admissao) >= 2016;