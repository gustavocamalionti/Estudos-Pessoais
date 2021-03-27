create database sucos_vendas;
use sucos_vendas;

/* É sempre interessante a gente visualizar e entender o banco, pra isso voce pode ir em database e reverse enginner para
criar um diagrama relacional e visualizar o banco de uma melhor forma*/
select * from itens_notas_fiscais;
select * from notas_fiscais;
select * from tabela_de_clientes;
select * from tabela_de_produtos;
select * from tabela_de_vendedores;

/*mesma seleção mas de modos diferentes*/
select cpf, nome, endereco_1, endereco_2, bairro, cidade, estado, cep, data_de_nascimento, idade, sexo, limite_de_credito, volume_de_compra, primeira_compra from tabela_de_clientes; 
select * from tabela_de_clientes;

/*Apenas campos selecionados*/
select cpf, nome from tabela_de_clientes;

/*apelido aos campos*/
select cpf as identificador_cliente, nome as nome_cliente from tabela_de_clientes;

/*Consultas Especificas*/
select * from tabela_de_produtos where codigo_do_produto = '1000889';
select * from tabela_de_produtos where sabor = 'Uva';
select * from tabela_de_produtos where sabor = 'Laranja';
select * from tabela_de_produtos where embalagem = 'Pet';
select * from tabela_de_produtos where preco_de_lista between 19.50 and 19.52;

