/*Relembrando alguns comandos...*/
use cursoemvideo;
describe cursos;
select*from gafanhotos;
select*from cursos;

/*inserindo registros*/
insert into cursos values 
(default, 'HTML4','Curso de HTML5', '40', '37', '2014'),
(default, 'Algoritmos','Lógica de Programação', '20', '15', '2014'),
(default, 'Photoshop', 'Dicas de Photoshop CC','10', '8', '2014'),
(default, 'PGP', 'Curso de PHP para iniciantes','40','20','2010'),
(default, 'Jarva', 'Introdução a Linguagem Java', '10', '29', '2000'),
(default,'MySQL', 'Banco de Dados MySQL', '30', '15', '2016'),
(default, 'Word', 'Curso completo de Word', '40', '30', '2016'),
(default, 'Sapateado', 'Danças Rítmicas', '40', '30', '2018'),
(default, 'Cozinha Árabe', 'Aprenda a fazer Kibe', '40', '30', '2018'),
(default, 'Youtuber', 'Gerar polêmica e ganhar inscritos', '5', '2', '2018');

select*from cursos;

/*Manipulando Linhas - renomeando um registro*/
/* em português: MODIFIQUE(update) OS cursos CONFIGURANDO(set) o nome para HTML5 ONDE(where) o id seja = 1*/
update cursos /*update = atualize*/
set nome = 'HTML5' /*set = configure*/
where idcurso = 1; /*where = onde*/

/*Alterando varios campos em um registro único*/
update cursos
set nome = 'PHP', ano = '2015'
where idcurso = '4';

update cursos
set nome = 'Java', carga = '40', ano = '2015'
where idcurso = '5'
limit 1;

/*alterando vários registros e campos diferentes*/
update cursos
set ano = 2050, carga = '800'
where ano = '2018';

/*Deletando uma linha específica*/
delete from cursos
where idcurso = '8';

/*Deletando várias linhas*/
/*Caso esteja dando  erro para deletar varias linhas de uma vez, segue edit-preferences-sqleditor-safeupdate (desmarcar)*/
delete from cursos
where ano = '2050'
limit 2;

truncate table cursos;
select*from cursos;
describe cursos;