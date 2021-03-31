select curdate() as resultado;
select current_time() as resultado;
select current_timestamp() as resultado;
select year(current_timestamp()) as resultado;
select day(current_timestamp()) as resultado;
select month(current_timestamp()) as resultado;
select monthname(current_timestamp()) as resultado;
select datediff('2022-01-24', current_timestamp()) as resultado;
SELECT datediff(current_timestamp(), '1999-01-24') as resultado;
select date_sub(current_timestamp(), interval 5 day) as resultado;

select distinct data_venda, 
dayname(data_venda) as DIA, monthname(data_venda) as MES, year(data_venda) as ANO 
from notas_fiscais;

select * from tabela_de_clientes;
/*Crie uma consulta que mostre o nome e a idade atual dos clientes.*/
select nome, datediff(year(current_timestamp()), year(data_de_nascimento)) from tabela_de_clientes;