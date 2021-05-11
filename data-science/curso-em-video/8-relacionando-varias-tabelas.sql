create database cadastro;
use cadastro;

describe cursos;
describe gafanhotos;

select * from cursos;
select * from gafanhotos;

create table gafanhotos_assiste_cursos (
id_assiste int not null auto_increment,
id_cursos int unique,
id_gafanhotos int,
data_assistido date,
primary key (id_assiste),
foreign key (id_cursos) references cursos(idcurso),
foreign key (id_gafanhotos) references gafanhotos(id));

select * from gafanhotos_assiste_cursos;
describe gafanhotos_assiste_cursos;

/*Modificando a posição de um campo já criado*/
alter table gafanhotos_assiste_cursos
modify column data_assistido date
after id_assiste;

/*Modificando a posição de um campo já criado*/
alter table gafanhotos_assiste_cursos
modify column id_gafanhotos int
after data_assistido;

alter table gafanhotos_assiste_cursos
modify column id_cursos int unique;

describe gafanhotos_assiste_cursos;
select * from gafanhotos_assiste_cursos;

insert into gafanhotos_assiste_cursos values
(default, '2014-03-01', '1', '2');

/*modo tradicional de visualizar e relacionar - inicial*/
select g.nome, c.idcurso, c.nome from gafanhotos as g
inner join gafanhotos_assiste_cursos as a
on a.id_gafanhotos = g.id
inner join cursos as c
on a.id_cursos = c.idcurso
order by g.nome;
;

/*renomeando os campos*/
select g.nome as nome_aluno, c.nome as nome_curso from gafanhotos as g
inner join gafanhotos_assiste_cursos as a
on a.id_gafanhotos = g.id
inner join cursos as c
on a.id_cursos = c.idcurso
order by g.nome;
;

delete from gafanhotos_assiste_cursos
where id_assiste = '7';