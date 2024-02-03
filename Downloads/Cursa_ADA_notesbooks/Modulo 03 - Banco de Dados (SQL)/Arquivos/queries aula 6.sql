
SELECT 
* -- colunas que queremos ver (TODAS = *)
FROM
pacientes -- tabela(s) que vamos consultar
-- WHERE -- SÓ SE QUERO FILTRAR
-- id_consulta BETWEEN 8 AND 12  -- id_consulta >= 8 and id_consulta =< 12
-- id_medico IN (1, 3) -- id_medico = 1 OR id_medico = 3
-- nome_paciente LIKE '%a%' -- paciente com pelo menos um 'a' no seu nome ------------
-- nome_paciente LIKE 'a%' -- paciente que o nome dele começa com 'a' ------------
-- EXTRACT(YEAR FROM data_nascimento) = 1990 
-- UPPER / LOWER
-- CONCAT(nome_paciente, '/' , genero) AS nome_genero
-- CAST(data_nascimento AS VARCHAR)  -------------

-- Me retorne todos os pacientes que fazem aniversario em julho. 
-- WHERE EXTRACT(MONTH FROM data_nascimento) = 7
-- Mostre o nome dele e a data de nascimento
-- Me retorne paciente que nasceram entre os anos 1995 e 2000
-- WHERE extract(year from data_nascimento) between 1995 and 2000

-- Retorne pacientes que o seu CPF começa com 5 (dica: cast e like)
WHERE cpf 

-- Retorne pacientes com endereço em uma Avenida e que tenham mais de 20 anos
-- (dica, comparação de Data com string, por exemplo WHERE data_nasicmento < '2000-01-01'
--  LIKE)

