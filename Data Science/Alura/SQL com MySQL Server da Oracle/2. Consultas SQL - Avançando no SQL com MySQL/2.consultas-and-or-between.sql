use sucos_vendas;
select * from tabela_de_produtos where sabor = 'Manga' or tamanho = '470 ml';
select * from tabela_de_produtos where sabor = 'Manga' and tamanho = '470 ml';
select * from tabela_de_produtos where not (sabor = 'Manga' or tamanho = '470 ml');
select * from tabela_de_produtos where not (sabor = 'Manga' and tamanho = '470 ml');
select * from tabela_de_produtos where sabor = 'Manga' and not (tamanho = '470 ml');

/*Mesmas Condições*/
select * from tabela_de_produtos where sabor IN ('Laranja', 'Manga');
select * from tabela_de_produtos where sabor = 'Laranja' or sabor = 'Manga';

select * from tabela_de_clientes where cidade in ('São Paulo', 'Rio de Janeiro') and idade >= 20;
select * from tabela_de_clientes where cidade in ('São Paulo', 'Rio de Janeiro') and (idade between 20 and 23);
select * from tabela_de_clientes where cidade in ('São Paulo', 'Rio de Janeiro') and (idade >= 29 or idade <= 20);
