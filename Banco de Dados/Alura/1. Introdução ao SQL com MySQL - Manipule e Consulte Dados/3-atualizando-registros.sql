use sucos;

update tbproduto 
set embalagem = 'Lata', preco_lista = 2.46
where produto = '544931';

update tbproduto
set embalagem = 'Garrafa'
where produto = '1078680';

select * from tbproduto;

update tabela_de_vendedores
set percentual_comissao = '0.11'
where matricula = '00236';

update tabela_de_vendedores
set nome = 'José Geraldo da Fonseca Junior'
where matricula = '00233';

select*from tabela_de_vendedores;