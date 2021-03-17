
/*Todo nome que começa com P*/
select*from cursos
where nome like 'P%'; /* like = parecido/semelhante - Wildcards = % Carta Coringa */

/*Todo nome que termina com P*/
select*from cursos
where nome like '%P';

/*Qualquer Registro que possui A/a em seu nome */
select*from cursos
where nome like '%a%';

/*Qualquer Registro que não possui A/a em seu nome */
select*from cursos
where nome not like '%a%';

update cursos
set nome = 'PáOO'
where idcurso= '9';

update cursos set nome = 'Photoshop5' where idcurso = '3';

/*Começa com PH, termina com P e termina com qualquer coisa após obrigatoriamente*/
select*from cursos
where nome like 'PH%P_'; 

/*Começa com p, termina com p, obrigatoriamente tem algum caracter entre eles e termina com alguma coisa*/
select*from cursos
where nome like 'p_p%';

select*from gafanhotos
where nome like '%Silva%';

select*from gafanhotos
where nome like '%_Silva';

select*from gafanhotos
where nome like '%Silva';

/*Selecionar somente 1 dos dados distintos*/
select distinct nacionalidade from gafanhotos 
order by nacionalidade;

select distinct carga from cursos
order by carga asc;

/*Funções de Agregação - Selecionar ou Totalizar alguma coisa*/
select count(*) from cursos;

select count(*)from cursos 
where carga > 40;

select max(carga) from cursos;

select min(carga) from cursos;

/*Dentro dos cursos de ano de 2016 o maior numero de aulas com nome */
select nome, max(totaulas) from cursos
where ano = '2016';

/*A soma de todas as totaulas de cada registro*/
select sum(totaulas) from cursos
where ano = '2016';

/*Tirar a Média AVG = Averege*/
select avg(totaulas) from cursos
where ano = '2016';