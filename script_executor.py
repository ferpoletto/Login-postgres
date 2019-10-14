CREATE DATABASE login;


CREATE TABLE USUARIOs (
	idusuario serial primary key,
	nome varchar(15) not null,
	senha varchar(30) not null,
	email varchar(30) not null,
	flinativo char not null
);

insert into usuarios(nome, senha, email, flinativo) values ('admin','admin', 'admin@admin', 'N' )
