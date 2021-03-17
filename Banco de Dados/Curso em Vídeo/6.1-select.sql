/*selecionando Campos Específicos*/
select nome, descricao, carga from cursos;

/*organizando em ordem decrescente*/
select*from cursos
order by ano desc;

/*Organizando em ordem Crescente*/
select id, nome, profissao, peso from gafanhotos
order by  peso asc; /*Não necessariamente precisa do asc*/


select ano, nome, carga from cursos
order by ano, nome;

select*from cursos
where ano = 2016
order by nome;

select nome, descricao, carga from cursos
where ano = 2016
order by carga;

/* Alguns Operadores*/
select nome, descricao, carga from cursos
where ano <= 2015 /*!= ou <> diferente;*/ 
order by ano, nome;

select nome, carga, ano  from cursos
where ano between 2016 and 2018
order by ano desc, nome asc;

select*from cursos
where ano in (2014,2016,2020)
order by ano asc, nome asc;

select nome, carga, totaulas from cursos
where carga > 35 and totaulas < 30;

select nome, carga, totaulas from cursos
where carga > 35 or totaulas < 30;
