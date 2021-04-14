use sucos_vendas;
 
select current_timestamp() as resultado;
 
 
select concat('O dia de hoje é: ',
date_format(current_timestamp(), '%d/%c/%y')) as resultado;
 
select concat('O dia de hoje é: ',
date_format(current_timestamp(), '%d/%m/%Y')) as resultado;
 
select concat('O dia de hoje é: ',
date_format(current_timestamp(), '%W, %d/%m/%Y')) as resultado;
  
select concat('O dia de hoje é: ',
date_format(current_timestamp(), '%W, %d/%m/%Y - %U')) as resultado; /*%U semana do ano*/

/*Convertendo em string*/
select convert(23.34, char) as resultado;

/*testando a conversão*/
select substring(convert(23.34, char), 1, 1) as resultado;

/*Queremos construir um SQL cujo resultado seja, para cada cliente:

“O cliente João da Silva faturou 120000 no ano de 2016”.

Somente para o ano de 2016.*/
select * from tabela_de_clientes;
select * from itens_notas_fiscais;
select * from notas_fiscais;

select 
concat('O cliente ', c.nome, ' faturou ', round(sum(b.preco*b.quantidade),2), ' no ano de ', year(a.data_venda), '.') as resultado
from notas_fiscais as a 
inner join itens_notas_fiscais as b on a.numero = b.numero
inner join tabela_de_clientes as c on c.cpf = a.cpf
where year(data_venda) = 2016
group by c.cpf
order by c.nome;