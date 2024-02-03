1. **DDL e DML**:
   - **DDL (Data Definition Language)**: Usado para definir a estrutura do banco de dados (criar, alterar ou excluir bancos de dados e tabelas).
   - **DML (Data Manipulation Language)**: Usado para manipular os dados dentro das tabelas (inserir, atualizar ou excluir registros).

   Exemplo DDL (criando uma tabela):
   ```python
   import mysql.connector

   conn = mysql.connector.connect(
       host="localhost",
       user="seu_usuario",
       password="sua_senha",
       database="seu_banco_de_dados"
   )

   cursor = conn.cursor()

   # Criando uma tabela
   cursor.execute("CREATE TABLE usuarios (id INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(255))")

   conn.close()
   ```

   Exemplo DML (inserindo dados):
   ```python
   import mysql.connector

   conn = mysql.connector.connect(
       host="localhost",
       user="seu_usuario",
       password="sua_senha",
       database="seu_banco_de_dados"
   )

   cursor = conn.cursor()

   # Inserindo dados
   cursor.execute("INSERT INTO usuarios (nome) VALUES ('João')")
   cursor.execute("INSERT INTO usuarios (nome) VALUES ('Maria')")

   conn.commit()
   conn.close()
   ```

2. **Databases**: Bancos de dados são contêineres que armazenam tabelas e dados relacionados. Você pode criar, selecionar e gerenciar bancos de dados.

   Exemplo de criação de banco de dados:
   ```python
   import mysql.connector

   conn = mysql.connector.connect(
       host="localhost",
       user="seu_usuario",
       password="sua_senha"
   )

   cursor = conn.cursor()

   # Criando um banco de dados
   cursor.execute("CREATE DATABASE meu_banco_de_dados")

   conn.close()
   ```

3. **Tabelas**: Tabelas são estruturas que armazenam dados em linhas e colunas.

   Exemplo de criação de tabela foi dado no tópico anterior.

4. **Primary e Foreign Keys**:
   - **Primary Key**: Uma coluna que identifica exclusivamente cada registro na tabela.
   - **Foreign Key**: Uma coluna que cria um relacionamento entre duas tabelas.

   Exemplo de criação de uma tabela com chaves primárias e estrangeiras:
   ```python
   cursor.execute("CREATE TABLE pedidos (id INT PRIMARY KEY, cliente_id INT, FOREIGN KEY (cliente_id) REFERENCES clientes(id))")
   ```

5. **Constraints**: Restrições aplicadas às colunas de uma tabela para impor regras de integridade de dados.

   Exemplo de adição de uma restrição UNIQUE:
   ```python
   cursor.execute("ALTER TABLE produtos ADD CONSTRAINT nome_unico UNIQUE (nome)")
   ```

6. **Inserção de dados**: Adicionar registros a uma tabela.

   Exemplo foi dado no tópico DML.

7. **Edição de dados**: Atualizar registros existentes em uma tabela.

   Exemplo de atualização de dados:
   ```python
   cursor.execute("UPDATE usuarios SET nome = 'José' WHERE id = 1")
   ```

8. **Exclusão de dados**: Remover registros de uma tabela.

   Exemplo de exclusão de dados:
   ```python
   cursor.execute("DELETE FROM usuarios WHERE id = 2")
   ```

9. **Consultas simples**:
   - Realizar consultas SELECT para recuperar dados da tabela.

   Exemplo de consulta simples:
   ```python
   cursor.execute("SELECT * FROM usuarios")
   result = cursor.fetchall()
   for row in result:
       print(row)
   ```

10. **MER e DER**: **MER (Modelo de Entidade e Relacionamento)** é uma representação visual de um banco de dados, enquanto **DER (Diagrama de Entidade e Relacionamento)** é uma versão simplificada do MER.

11. **Formas normais**: Conjunto de regras para projetar bancos de dados para eliminar redundância e melhorar a eficiência.

12. **JOINS**: Combinação de dados de duas ou mais tabelas com base em colunas relacionadas.

   Exemplo de JOIN:
   ```python
   cursor.execute("SELECT pedidos.id, clientes.nome FROM pedidos JOIN clientes ON pedidos.cliente_id = clientes.id")
   ```

13. **Union**: Combinação de resultados de duas ou mais consultas SELECT.

   Exemplo de UNION:
   ```python
   cursor.execute("SELECT nome FROM clientes UNION SELECT nome FROM fornecedores")
   ```

14. **Agregação**: Usado com funções como COUNT, SUM, AVG, etc., para resumir dados em consultas.

   Exemplo de agregação (contagem de registros):
   ```python
   cursor.execute("SELECT COUNT(*) FROM pedidos")
   ```

15. **Cast**: Conversão de um tipo de dado em outro.

   Exemplo de CAST:
   ```python
   cursor.execute("SELECT nome, CAST(id AS CHAR) FROM usuarios")
   ```

16. **Views**: Tabelas virtuais que armazenam consultas SQL. São usadas para simplificar consultas complexas.

   Exemplo de criação de uma view:
   ```python
   cursor.execute("CREATE VIEW v_pedidos AS SELECT id, cliente_id FROM pedidos WHERE status = 'ativo'")
   ```

Aqui estão os exemplos organizados como explicações:

**Exemplo 1: Consulta com Alias e Ordenação**
Neste exemplo, estamos selecionando dados da tabela "emprestimo". Renomeamos algumas colunas usando aliases e ordenamos o resultado pelo sexto campo (a diferença entre as datas de devolução e empréstimo).

```sql
select
	emprestimo.id_usuario as 'Cod. Usuário',
	dt_emprestimo as 'Data de Empréstimo',
	dt_devolucao as 'Data de Devolução',
    id_emprestimo,
	dt_devolucao - dt_emprestimo as 'subtracao mysql',
	datediff(dt_devolucao, dt_emprestimo) as 'Dias para Devolução' 	
from emprestimo
order by 6;
```

**Exemplo 2: Extração de Componentes de Data**
Neste exemplo, estamos extraindo componentes de data (ano, mês e dia) da coluna "dt_emprestimo" da tabela "emprestimo".

```sql
select
	id_usuario,
	dt_emprestimo,
    year(dt_emprestimo) as ano,
    month(dt_emprestimo) as mes,
    day(dt_emprestimo) as dia
from emprestimo;
```

**Exemplo 3 e 4: Formatação de CPF, Manipulação de Texto e Cálculo de Idade**
Nesses exemplos, estamos formatando o CPF, manipulando o texto do nome do usuário e calculando a idade dos usuários com base na data de nascimento. O primeiro exemplo filtra usuários nascidos a partir de 2000, enquanto o segundo filtra usuários nascidos em determinados meses.

**Exemplo 5: Filtragem por Mês de Nascimento**
Neste exemplo, estamos filtrando usuários cujo mês de nascimento não seja setembro.

**Exemplo 6: Filtragem de Registros com CPF Válido**
Neste exemplo, estamos filtrando registros da tabela "usuario" onde o CPF não é nulo e não está vazio.

**Exemplo 7: Extração do Último Nome**
Neste exemplo, estamos extraindo o último nome dos usuários da tabela "usuario" usando a função `substring_index`.

**Exemplo 8: Agregação de Dados de Empréstimo**
Neste exemplo, estamos realizando várias operações de agregação na tabela "emprestimo", como contagem de empréstimos, contagem de usuários distintos e identificação da primeira e última data de empréstimo.

**Exemplo 9: Consulta com Limite e Ordenação**
Neste exemplo, estamos selecionando os três registros mais recentes da tabela "emprestimo" e ordenando-os por data de empréstimo decrescente.

**Exemplo 10: Contagem de Empréstimos por Usuário em 2023**
Neste exemplo, estamos contando o número de empréstimos por usuário em 2023 e ordenando o resultado por usuário.

**Exemplo 11: Usuário com Mais Empréstimos em 2023**
Neste exemplo, estamos encontrando o usuário com mais empréstimos em 2023, limitando o resultado a um único registro.

**Exemplo 12: Estatísticas de Empréstimo por Usuário**
Neste exemplo, estamos calculando estatísticas de empréstimo por usuário, incluindo a média, a devolução mais rápida, a devolução mais demorada e categorizando os clientes com base no número de empréstimos.

**Exemplo 13 e 14: Consultas com Junção de Tabelas**
Nesses exemplos, estamos realizando consultas que envolvem junção de tabelas "emprestimo" e "usuario" com várias condições de filtro.

**Exemplo 15: Inserção de Dados na Tabela "usuario"**
Neste exemplo, estamos inserindo um novo registro na tabela "usuario" com informações como CPF, nome, telefone e data de nascimento.

**Exemplo 16: Consulta com Junção de Múltiplas Tabelas e Agrupamento**
Neste exemplo, estamos realizando uma consulta complexa que envolve várias tabelas (usuario, emprestimo, livro, autor, genero) com junções e agregações.

**Exemplo 17: Criação de uma Visualização (View)**
Neste exemplo, estamos criando uma visualização chamada "vw_genero_usuario" que encapsula a consulta complexa realizada anteriormente.

**Exemplo 18: Inserção de Dados na Tabela "emprestimo"**
Neste exemplo, estamos inserindo um novo registro na tabela "emprestimo" com informações de data e ID de usuário.

**Exemplo 19 e 20: Consultas de Processos e Finalização**
Nesses exemplos, estamos mostrando processos em execução (processlist) e demonstrando como finalizar um processo específico (kill).

**Exemplos 21 a 26: Tipos de Junção (INNER, LEFT, RIGHT, FULL) e UNION**
Esses exemplos ilustram diferentes tipos de junção (INNER, LEFT, RIGHT, FULL) entre as tabelas "categoria" e "produto". O último exemplo combina os resultados da junção LEFT e RIGHT usando UNION.

**Exemplo 27: Consulta com CROSS JOIN**
Neste exemplo, estamos realizando uma consulta que utiliza CROSS JOIN entre as tabelas "categoria" e "produto".

**Exemplo 28: Criação de uma Visualização com Junção FULL**
Neste exemplo, estamos criando uma visualização chamada "vw_full_join" que encapsula uma consulta complexa envolvendo junção FULL entre as tabelas "categoria" e "produto".
