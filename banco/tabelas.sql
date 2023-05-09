use CavaloLivre

create table produto (
	id int primary key auto_increment not null,
	nome varchar(100),
	preco float,
	descricao varchar(1000),
	imagens varchar(10000)
);

create table categoria (
	id int primary key auto_increment not null,
	nome varchar(100)
);

create table produto_x_categoria (
	id int primary key auto_increment not null,
	id_produto int,
	id_categoria int,
	foreign key (id_produto) references produto(id),
	foreign key (id_categoria) references categoria(id)
);

create table cliente (
	id int primary key auto_increment not null,
	nome varchar(100),
	sobrenome varchar(100),
	email varchar(100),
	senha varchar(100),
	nascimento date,
	pais varchar(100),
	sexo varchar(100)
);

create table pedido (
	id int primary key auto_increment not null,
	id_cliente int,
	foreign key (id_cliente) references cliente(id)
);

create table item (
	id int primary key auto_increment not null,
	quantidade int,
	valor_unitario float,
	id_pedido int,
	id_produto int,
	foreign key (id_pedido) references pedido(id),
	foreign key (id_produto) references produto(id)
);
