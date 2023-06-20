create database CavaloLivre;

use CavaloLivre;

create table produto (
	id int primary key auto_increment not null,
	nome varchar(100) not null,
	preco float not null,
	descricao varchar(1000) not null,
	imagens varchar(10000) not null
);

create table categoria (
	id int primary key auto_increment not null,
	nome varchar(100) not null
);

create table produto_x_categoria (
	id int primary key auto_increment not null,
	id_produto int not null,
	id_categoria int not null,
	foreign key (id_produto) references produto(id),
	foreign key (id_categoria) references categoria(id)
);

create table cliente (
	id int primary key auto_increment not null,
	nome varchar(100) not null,
	sobrenome varchar(100) not null,
	email varchar(100) unique not null,
	senha varchar(100) not null,
	nascimento date not null,
	pais varchar(100) not null,
	sexo varchar(100) not null
);

create table pedido (
	id int primary key auto_increment not null,
	id_cliente int not null,
	foreign key (id_cliente) references cliente(id)
);

create table item (
	id int primary key auto_increment not null,
	quantidade int not null,
	valor_unitario float not null,
	id_pedido int not null,
	id_produto int not null,
	foreign key (id_pedido) references pedido(id),
	foreign key (id_produto) references produto(id)
);

create table sessao (
	id int primary key auto_increment not null,
	token varchar(200) unique not null,
	id_cliente int not null,
	foreign key (id_cliente) references cliente(id)
);