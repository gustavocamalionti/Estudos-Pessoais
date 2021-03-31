use sucos_vendas;

select * from tabela_de_clientes;
select * from notas_fiscais;

select count(*) from tabela_de_clientes;

select cpf, count(*) from notas_fiscais group by cpf;

select distinct 
a.cpf, a.nome, b.cpf 
from tabela_de_clientes as a 
left outer join notas_fiscais as b 
on b.cpf = a.cpf;

/*Trazer todos os resultados que nunca compraram na empresa*/
select distinct 
a.cpf, a.nome, b.cpf 
from tabela_de_clientes as a 
left outer join notas_fiscais as b 
on b.cpf = a.cpf
where b.cpf is null;
 
/*Trazer todos os resultados que nunca compraram em 2015 */
select distinct 
a.cpf, a.nome, b.cpf 
from tabela_de_clientes as a 
left outer join notas_fiscais as b 
on b.cpf = a.cpf
where b.cpf is null and year(b.data_venda) = 2015;

/*Usando right outer join*/
select distinct 
a.cpf, a.nome, b.cpf
from tabela_de_clientes as a
right outer join notas_fiscais as b
on b.cpf = a.cpf;

