use sucos;
select * from tbproduto where preco_lista between 16.007 and 16.009;
select * from tbproduto where preco_lista >= 16.009 and preco_lista <= 16.009;

select * from tbcliente where idade >= '19' and idade <= '22';
select * from tbcliente where (idade >= '19' and idade <= '22') and sexo = 'M';

select * from tbcliente where cidade = 'Rio de Janeiro' or bairro = 'Jardins';

select * from tbcliente where (idade >= '19' and idade <= '22') and (cidade = 'Rio de Janeiro' or bairro = 'Jardins'); 

describe tabela_de_vendedores;

select nome, data_admissao from tabela_de_vendedores where year(data_admissao) <2016 and de_ferias = '1';