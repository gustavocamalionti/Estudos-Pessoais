use cadastro;
select * from cursos;

select nome, totaulas, count(*) from cursos
group by totaulas
order by totaulas desc;

select * from cursos where totaulas > '20';

select carga, count(totaulas) from cursos /*Alternativa >>>>>>> count(*)*/
where totaulas = '30'
group by carga;

select * from cursos where carga = '60';

select ano, count(*) from cursos
group by ano
having count(*) >= 3
order by count(*) desc;

select nome, ano, totaulas, count(*) from cursos
where totaulas >= 28
group by ano
having ano >= 2014
order by count(*) desc;

select avg(carga) from cursos;

select nome, carga, count(*) from cursos 
where ano > 2015
group by carga
having carga >= (select avg(carga) from cursos)
order by count(*);