/*inserindo dados - INSIRA NA TABELA pessoas (.........) OS VALORES*/
insert into pessoas
(nome, nascimento, sexo, peso, altura)
values
('Felix Gonçalves', '1999-04-29', 'm', '60.5', '1.68');

/*Selecione(select) Tudo(*) De(from) pessoas*/
select*from pessoas;

/*Deletando um registro na tabela*/
delete from pessoas where id=4;

/*Adicionando vários registros de uma vez*/
insert into pessoas
(id, nome, nascimento, sexo, peso, altura, nacionalidade)
values
(default, 'Joas', '1997-03-13', 'm', '78', '1.67', default),
('3', 'Lucas', '1997-03-13', 'm', '90', '1.85', 'EUA'),
(default, 'Guilherme', '1997-03-13', 'm', '80.89', '1.90', 'Brasil'),
('4', 'Maria', '1997-03-13', 'f', '50', '1.63', default);

select*from pessoas;

/*MANEIRA SIMPLIFICADA*/
insert into pessoas values (default, 'Mariana', '2000-02-23', 'f', '80', '1.67', default);

SELECT*FROM pessoas; 