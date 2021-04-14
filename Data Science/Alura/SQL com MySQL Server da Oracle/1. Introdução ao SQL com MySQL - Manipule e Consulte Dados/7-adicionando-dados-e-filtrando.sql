use sucos;

describe tbcliente;
describe tbproduto;

select * from tbcliente;
select * from tbproduto;

/*Inserindo registros na tabela tbcliente*/
INSERT INTO tbcliente (CPF,NOME,ENDERECO1,ENDERECO2,BAIRRO,CIDADE,ESTADO,CEP,DATA_NASCIMENTO,IDADE,SEXO,LIMITE_CREDITO,VOLUME_COMPRA,PRIMEIRA_COMPRA) VALUES 
('19290992743','Fernando Cavalcante','R. Dois de Fevereiro','','Água Santa','Rio de Janeiro','RJ','22000000','2000-02-12',18,'M',100000,200000,1),
('2600586709','César Teixeira','Rua Conde de Bonfim','','Tijuca','Rio de Janeiro','RJ','22020001','2000-03-12',18,'M',120000,220000,0),
('95939180787','Fábio Carvalho','R. dos Jacarandás da Península','','Barra da Tijuca','Rio de Janeiro','RJ','22002020','1992-01-05',16,'M',90000,180000,1),
('9283760794','Edson Meilelles','R. Pinto de Azevedo','','Cidade Nova','Rio de Janeiro','RJ','22002002','1995-10-07',22,'M',150000,250000,1),
('7771579779','Marcelo Mattos','R. Eduardo Luís Lopes','','Brás','São Paulo','SP','88202912','1992-03-25',25,'M',120000,200000,1),
('5576228758','Petra Oliveira','R. Benício de Abreu','','Lapa','São Paulo','SP','88192029','1995-11-14',22,'F',70000,160000,1),
('8502682733','Valdeci da Silva','R. Srg. Édison de Oliveira','','Jardins','São Paulo','SP','82122020','1995-10-07',22,'M',110000,190000,0),
('1471156710','Érica Carvalho','R. Iriquitia','','Jardins','São Paulo','SP','80012212','1990-09-01',27,'F',170000,245000,0),
('3623344710','Marcos Nougeuira','Av. Pastor Martin Luther King Junior','','Inhauma','Rio de Janeiro','RJ','22002012','1995-01-13',23,'M',110000,220000,1),
('50534475787','Abel Silva ','Rua Humaitá','','Humaitá','Rio de Janeiro','RJ','22000212','1995-09-11',22,'M',170000,260000,0),
('5840119709','Gabriel Araujo','R. Manuel de Oliveira','','Santo Amaro','São Paulo','SP','80010221','1985-03-16',32,'M',140000,210000,1),
('94387575700','Walber Lontra','R. Cel. Almeida','','Piedade','Rio de Janeiro','RJ','22000201','1989-06-20',28,'M',60000,120000,1),
('8719655770','Carlos Eduardo','Av. Gen. Guedes da Fontoura','','Jardins','São Paulo','SP','81192002','1983-12-20',34,'M',200000,240000,0),
('5648641702','Paulo César Mattos','Rua Hélio Beltrão','','Tijuca','Rio de Janeiro','RJ','21002020','1991-08-30',26,'M',120000,220000,0),
('492472718','Eduardo Jorge','R. Volta Grande','','Tijuca','Rio de Janeiro','RJ','22012002','1994-07-19',23,'M',75000,95000,1);

/*Inserindo Registros na tabela tbproduto*/
INSERT INTO tbproduto (PRODUTO, NOME, EMBALAGEM, TAMANHO, SABOR, PRECO_LISTA) VALUES 
('1078680','Frescor do Verão - 470 ml - Manga','Garrafa','470 ml','Manga',5.1795),
('1042712','Linha Citros - 700 ml - Limão','Garrafa','700 ml','Limão',4.904),
('788975','Pedaços de Frutas - 1,5 Litros - Maça','PET','1,5 Litros','Maça',18.011),
('1002767','Videira do Campo - 700 ml - Cereja/Maça','Garrafa','700 ml','Cereja/Maça',8.41),
('231776','Festival de Sabores - 700 ml - Açai','Garrafa','700 ml','Açai',13.312),
('479745','Clean - 470 ml - Laranja','Garrafa','470 ml','Laranja',3.768),
('1051518','Frescor do Verão - 470 ml - Limão','Garrafa','470 ml','Limão',3.2995),
('1101035','Linha Refrescante - 1 Litro - Morango/Limão','PET','1 Litro','Morango/Limão',9.0105),
('229900','Pedaços de Frutas - 350 ml - Maça','Lata','350 ml','Maça',4.211),
('1086543','Linha Refrescante - 1 Litro - Manga','PET','1 Litro','Manga',11.0105),
('695594','Festival de Sabores - 1,5 Litros - Açai','PET','1,5 Litros','Açai',28.512),
('838819','Clean - 1,5 Litros - Laranja','PET','1,5 Litros','Laranja',12.008),
('326779','Linha Refrescante - 1,5 Litros - Manga','PET','1,5 Litros','Manga',16.5105),
('520380','Pedaços de Frutas - 1 Litro - Maça','PET','1 Litro','Maça',12.011),
('1041119','Linha Citros - 700 ml - Lima/Limão','Garrafa','700 ml','Lima/Limão',4.904),
('243083','Festival de Sabores - 1,5 Litros - Maracujá','PET','1,5 Litros','Maracujá',10.512),
('394479','Sabor da Montanha - 700 ml - Cereja','Garrafa','700 ml','Cereja',8.409),
('746596','Light - 1,5 Litros - Melância','PET','1,5 Litros','Melância',19.505),
('773912','Clean - 1 Litro - Laranja','PET','1 Litro','Laranja',8.008),
('826490','Linha Refrescante - 700 ml - Morango/Limão','Garrafa','700 ml','Morango/Limão',6.3105),
('723457','Festival de Sabores - 700 ml - Maracujá','Garrafa','700 ml','Maracujá',4.912),
('812829','Clean - 350 ml - Laranja','Lata','350 ml','Laranja',2.808),
('290478','Videira do Campo - 350 ml - Melância','Lata','350 ml','Melância',4.56),
('783663','Sabor da Montanha - 700 ml - Morango','Garrafa','700 ml','Morango',7.709),
('235653','Frescor do Verão - 350 ml - Manga','Lata','350 ml','Manga',3.8595),
('1002334','Linha Citros - 1 Litro - Lima/Limão','PET','1 Litro','Lima/Limão',7.004),
('1013793','Videira do Campo - 2 Litros - Cereja/Maça','PET','2 Litros','Cereja/Maça',24.01),
('1096818','Linha Refrescante - 700 ml - Manga','Garrafa','700 ml','Manga',7.7105),
('1022450','Festival de Sabores - 2 Litros - Açai','PET','2 Litros','Açai',38.012);

select * from tbcliente;

select cpf, nome, endereco1, endereco2, bairro, cidade, estado, cep, idade, sexo, limite_credito, volume_compra, primeira_compra, data_nascimento from tbcliente;
select cpf, nome from tbcliente;

select cpf, nome from tbcliente
limit 5;

select cpf as cpf_cliente, nome as nome_cliente from tbcliente;

select nome, matricula from tabela_de_vendedores;

select * from tbproduto
where produto = '544931';

SELECT * FROM tbcliente 
where cidade = 'Rio de Janeiro';

select*from tbproduto 
where sabor = 'Limao';

update tbproduto 
set sabor = 'Citrus' 
where sabor = 'Limão';

select * from tbproduto;

select * from tabela_de_vendedores where nome = 'Cláudia Morais';

