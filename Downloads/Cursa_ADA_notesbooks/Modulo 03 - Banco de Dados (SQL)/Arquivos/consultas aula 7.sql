-- STRING -> POR CADA CARACTERE 11byte
-- INTEGER -> 4 E 8 bytes   

CREATE TABLE pacientes (
	id_paciente INTEGER PRIMARY KEY,
    nome_paciente VARCHAR(80), 
	data_nascimento DATE,
	genero VARCHAR(2),
	CPF INTEGER,
	endereco VARCHAR(128),
	telefone VARCHAR(80),
	email VARCHAR (64)
);

CREATE TABLE doencas (
	cid VARCHAR(20) PRIMARY KEY,
	nome_doenca VARCHAR(128),
	descricao VARCHAR(256)
);

CREATE TABLE medicos (
	id_medico INTEGER PRIMARY KEY,
	nome_medico VARCHAR(80),
	espcialidade VARCHAR(50),
	crm VARCHAR(16)
);

CREATE TABLE consultas (
	id_consulta INTEGER PRIMARY KEY,
	id_paciente INTEGER,
	id_medico INTEGER,
	data_consulta TIMESTAMP,
	cid VARCHAR(20),
	diagnostico VARCHAR(200),
	prescricao VARCHAR(200),
	retorno BOOLEAN
);
 
INSERT INTO pacientes (id_paciente, nome_paciente, data_nascimento, genero, CPF, endereco, telefone, email) 
VALUES 
(1, 'João Silva', '1990-05-15', 'M', 12345678901, 'Rua A, 123', '(XX)XXXXX-XXXX', 'joao@email.com'),
(2, 'Maria Santos', '1985-08-20', 'F', 98765432109, 'Avenida B, 456', '(YY)YYYYY-YYYY', 'maria@email.com'),
(3, 'Pedro Oliveira', '2000-12-10', 'M', 34567890123, 'Rua C, 789', '(ZZ)ZZZZZ-ZZZZ', 'pedro@email.com'),
(4, 'Ana Souza', '1992-03-25', 'F', 45678901234, 'Praça D, 56', '(WW)WWWWW-WWWW', 'ana@email.com'),
(5, 'Luiz Ferreira', '1988-11-18', 'M', 89012345678, 'Avenida E, 789', '(VV)VVVVV-VVVV', 'luiz@email.com'),
(6, 'Carolina Lima', '1995-07-08', 'F', 56789012345, 'Rua F, 101', '(UU)UUUUU-UUUU', 'carolina@email.com'),
(7, 'Rafaela Costa', '1980-09-30', 'F', 23456789012, 'Rua G, 22', '(TT)TTTTT-TTTT', 'rafaela@email.com'),
(8, 'Gabriel Santos', '1976-12-14', 'M', 67890123456, 'Avenida H, 321', '(SS)SSSSS-SSSS', 'gabriel@email.com'),
(9, 'Juliana Oliveira', '1998-04-05', 'F', 78901234567, 'Praça I, 45', '(RR)RRRRR-RRRR', 'juliana@email.com'),
(10, 'Daniel Martins', '1983-06-22', 'M', 32109876543, 'Rua J, 15', '(QQ)QQQQQ-QQQQ', 'daniel@email.com');


INSERT INTO consultas (id_consulta, id_paciente, id_medico, data_consulta, cid, diagnostico, prescricao, retorno) 
VALUES 
(4, 1, 2, '2023-04-15 10:20:00', 'C001', 'Resfriado', 'Descanso e medicamento sintomático', FALSE),
(5, 3, 1, '2023-05-02 08:45:00', 'C002', 'Avaliação cardiológica', 'Exames complementares', TRUE),
(6, 2, 3, '2023-06-18 15:30:00', 'C003', 'Controle glicêmico', 'Revisão de medicação', FALSE),
(7, 4, 2, '2023-07-10 11:00:00', 'C001', 'Infecção respiratória', 'Antibióticos e repouso', FALSE),
(8, 5, 1, '2023-08-25 09:20:00', 'C002', 'Hipertensão', 'Medicação anti-hipertensiva', TRUE),
(9, 6, 3, '2023-09-14 14:00:00', 'C003', 'Diabetes tipo 1', 'Insulina e monitoramento', FALSE),
(10, 7, 2, '2023-10-03 10:45:00', 'C001', 'Resfriado com complicações', 'Repouso e acompanhamento', FALSE),
(11, 8, 1, '2023-11-20 08:00:00', 'C002', 'Pressão arterial elevada', 'Medicação e controle de dieta', TRUE),
(12, 9, 3, '2023-12-12 16:30:00', 'C003', 'Diabetes gestacional', 'Orientações e dieta especializada', FALSE),
(13, 10, 2, '2023-12-30 13:15:00', 'C001', 'Resfriado com febre alta', 'Medicação e hidratação', FALSE);

INSERT INTO doencas (cid, nome_doenca, descricao) 
VALUES 
('C001', 'Gripe', 'Infecção viral comum'),
('C002', 'Hipertensão', 'Pressão arterial elevada'),
('C003', 'Diabetes', 'Problema de metabolismo de açúcar');

INSERT INTO medicos (id_medico, nome_medico, espcialidade, crm) 
VALUES 
(1, 'Dr. Ana Souza', 'Clínica Geral', 'CRM12345'),
(2, 'Dr. Carlos Mendes', 'Cardiologia', 'CRM54321'),
(3, 'Dra. Laura Ferreira', 'Dermatologia', 'CRM98765');

