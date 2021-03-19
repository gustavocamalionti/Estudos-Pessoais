/*selecionando Campos Específicos*/
select nome, descricao, carga from cursos;

/*Organizando em ordem Crescente*/
select id, nome, profissao, peso from gafanhotos
order by  peso asc; /*Não necessariamente precisa do asc*/


/*organizando em ordem decrescente*/
select*from cursos
order by ano desc;

/* organização por ano e depois por nome*/
select ano, nome, carga from cursos
order by ano, nome;

/*Selecionar por nome apenas os registros de 2016*/
select*from cursos
where ano = 2016
order by nome;

/*selecionar por carga apenas os registros de 2016*/
select nome, descricao, carga from cursos
where ano = 2016
order by carga;

/* Alguns Operadores*/
select nome, descricao, carga from cursos
where ano <= 2015 /*!= ou <> diferente;*/ 
order by ano, nome;

/*between*/
select nome, carga, ano  from cursos
where ano between 2016 and 2018 /* between = entre */
order by ano desc, nome asc; /* desc = ascendent / asc = ascendent */

/*in*/
select*from cursos
where ano in (2014,2016,2020)
order by ano asc, nome asc;

/* '<', '>', e 'and'*/
select nome, carga, totaulas from cursos
where carga > 35 and totaulas < 30;

/*'or'*/
select nome, carga, totaulas from cursos
where carga > 35 or totaulas < 30;
