use cadastro;
describe gafanhotos;

alter table gafanhotos
add column cursopreferido int;

alter table gafanhotos
add foreign key (cursopreferido) 
references cursos(idcurso);

select * from gafanhotos;

select * from cursos;

update gafanhotos set cursopreferido = '6' where id = '1';

/*Erro de Integridade Referencial*/ 
delete from cursos where idcurso = '6';

delete from cursos where idcurso = '9';

/*Junções*/
select nome, cursopreferido from gafanhotos;
select nome, ano from cursos;

/* Junção sem Filtragem */
select gafanhotos.nome, gafanhotos.cursopreferido, cursos.nome, cursos.ano from gafanhotos join cursos;

/* Dando sentido para as Junções - INNER JOIN SÓ MOSTRA OS REGISTROS COM RELAÇÕES ENTRE TABELAS */
select gafanhotos.nome, gafanhotos.cursopreferido, cursos.nome, cursos.ano 
from gafanhotos inner join cursos
on cursos.idcurso = gafanhotos.cursopreferido
order by gafanhotos.nome desc;

/**/ 
select g.nome, g.cursopreferido, c.nome, c.ano
from gafanhotos as g inner join cursos as c
on c.idcurso = g.cursopreferido
order by g.nome desc;

