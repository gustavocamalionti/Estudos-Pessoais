use sucos;

/*Inserindo 1 valor apenas*/
insert into tbproduto (produto, nome, embalagem, tamanho, sabor, preco_lista) 
values ('1040107', 'Light - 350 ml - Melância', 'Lata', '350 ml', 'melância', 4.56);

select * from tbproduto;

insert into tabela_de_vendedores (matricula, nome, percentual_comissao) 
values ('00233', 'João Geraldo da Fonseca', 0.1);

select * from tabela_de_vendedores;

/*Inserindo Vários Valores*/
insert into tbproduto (produto, nome, embalagem, tamanho, sabor, preco_lista) values 
('1037797', 'Clean - 2 Litros - Laranja', 'PET', '2 Litros', 'Laranja', 16.008),
('1000889', 'Sabor da Montanha - 700 ml - Uva', 'Garrafa', '700 ml', 'Uva', 6.31),
('1004327', 'Videira do Campo - 1,5 Litros - Melância', 'PET', '1,5 Litros', 'Melância', 19.51);

describe tbproduto;
select*from tbproduto;

insert into tabela_de_vendedores (matricula, nome, percentual_comissao) values 
('00235', 'Márcia Almeida da Silva', 0.08),
('00236', 'Cláudia Morais', 0.08);

select*from tabela_de_vendedores;

/*inserindo registros com campos preenchidos incorretamente*/
insert into tbproduto values
('544931', 'Frescor do Verão - 350 ml - Limão', 'PET', '350 ml','Limão',3.20),
('1078680', 'Frescor do Verão - 470 ml - Manga', 'Lata', '470 ml','Manga',5.18);

select*from tbproduto;

