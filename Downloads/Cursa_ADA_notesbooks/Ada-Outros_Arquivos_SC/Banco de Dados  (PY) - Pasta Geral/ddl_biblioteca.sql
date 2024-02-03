CREATE TABLE editora 
( 
 id_editora INT PRIMARY KEY AUTO_INCREMENT,  
 nome_editora VARCHAR(200)  
); 

CREATE TABLE livro 
( 
 id_livro INT PRIMARY KEY AUTO_INCREMENT,  
 isbn VARCHAR(200),  
 nome_livro VARCHAR(200),  
 qtde_disponivel INT,  
 faixa_etaria INT  
); 

CREATE TABLE autor 
( 
 id_autor INT PRIMARY KEY AUTO_INCREMENT,  
 nome_autor VARCHAR(200)  
); 

CREATE TABLE emprestimo 
( 
 id_emprestimo INT PRIMARY KEY AUTO_INCREMENT,  
 dt_emprestimo DATE NOT NULL,  
 dt_devolucao DATE,  
 id_usuario INT  
); 

CREATE TABLE usuario 
( 
 id_usuario INT PRIMARY KEY AUTO_INCREMENT,
 cpf VARCHAR(20),  
 nome_usuario VARCHAR(200) NOT NULL,  
 telefone_usuario VARCHAR(200),  
 dt_nascimento DATE NOT NULL  
); 

CREATE TABLE genero 
( 
 id_genero INT PRIMARY KEY AUTO_INCREMENT,  
 nome_genero VARCHAR(200)  
); 

CREATE TABLE livro_editora 
( 
 id_livro INT,  
 id_editora INT  
); 

CREATE TABLE livro_genero 
( 
 id_livro INT,  
 id_genero INT  
); 

CREATE TABLE livro_autor 
( 
 id_livro INT,  
 id_autor INT  
); 

CREATE TABLE livro_emprestimo 
( 
 id_livro INT,  
 id_emprestimo INT 
); 

ALTER TABLE emprestimo ADD FOREIGN KEY(id_usuario) REFERENCES usuario (id_usuario)
ALTER TABLE livro_editora ADD FOREIGN KEY(id_livro) REFERENCES livro (id_livro)
ALTER TABLE livro_editora ADD FOREIGN KEY(id_editora) REFERENCES editora (id_editora)
ALTER TABLE livro_genero ADD FOREIGN KEY(id_livro) REFERENCES livro (id_livro)
ALTER TABLE livro_genero ADD FOREIGN KEY(id_genero) REFERENCES genero (id_genero)
ALTER TABLE livro_autor ADD FOREIGN KEY(id_livro) REFERENCES livro (id_livro)
ALTER TABLE livro_autor ADD FOREIGN KEY(id_autor) REFERENCES autor (id_autor)
ALTER TABLE livro_emprestimo ADD FOREIGN KEY(id_livro) REFERENCES livro (id_livro)
ALTER TABLE livro_emprestimo ADD FOREIGN KEY(id_emprestimo) REFERENCES emprestimo (id_emprestimo)