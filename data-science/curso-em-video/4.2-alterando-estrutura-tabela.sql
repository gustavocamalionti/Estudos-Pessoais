/*Visualizações*/
use cursoemvideo;
describe gafanhotos;
select*from gafanhotos;

create table if not exists cursos (
nome varchar(30) not null unique,
descricao text,
carga int unsigned,
totaulas int,
ano year default '2021');

alter table cursos
add column idcurso int first;

alter table cursos
add primary key (idcurso);

alter table cursos
modify idcurso int auto_increment first;

describe cursos;

create table if not exists teste(
idtest int  not null auto_increment,
nome varchar(30) not null,
sexo enum('F','M'),
nascimento year,
primary key (idtest));

alter table teste
modify column nascimento date;


insert into teste values 
(default, 'Marcos', 'm', '2000-03-28'),
(default, 'Mariana', 'F', '2000-02-23'),
(default, 'Maricota', 'f', '1975-03-30');

select*from teste;

alter table teste
modify sexo enum('f','m','b');

drop table if exists alunos;

drop table if exists teste; 