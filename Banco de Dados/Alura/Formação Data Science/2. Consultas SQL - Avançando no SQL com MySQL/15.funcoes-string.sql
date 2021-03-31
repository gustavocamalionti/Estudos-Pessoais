use sucos_vendas;

select ltrim('     Olá') as RESULTADO;
select rtrim('Olá     ') as RESULTADO;
select trim('     Olá   ') as RESULTADO;
select concat('Olá',' ', 'Tudo Bem?', 'sim') as RESULTADO;
select upper ('Olá, tudo bem?') as RESULTADO;
select lower('Olá, tudo  bem?') as RESULTADO;
select substring('Olá, tudo bem?',5) as RESULTADO;
select substring('Olá, tudo bem?',6, 4) as RESULTADO;
select concat(Nome, ' (', CPF, ') ') as RESULTADO from tabela_de_clientes; 

select * from tabela_de_clientes;
/*Faça uma consulta listando o nome do cliente e o endereço completo (Com rua, bairro, cidade e estado).*/
select concat(nome, ' ', endereco_1, ' ', bairro, ' ', cidade, '-', estado) as RESULTADO from tabela_de_clientes;