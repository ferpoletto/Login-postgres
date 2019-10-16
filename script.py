create table usuario(
id serial primary KEY,
nome varchar(30) not null,
senha varchar(30) not null,
email varchar(30) not null,
flinativo char not null)

insert into usuario values (1,'admin', 'admin', 'admin@admin', 'N')