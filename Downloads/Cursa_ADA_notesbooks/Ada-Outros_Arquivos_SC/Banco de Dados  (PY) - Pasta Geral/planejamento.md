
**Sprint 3: Consultas SQL (4 horas)**

7. **1 hora**: Configurar um ambiente de banco de dados MySQL, se ainda não o tiver feito.
8. **1 hora**: Criar as tabelas "produtos", "categorias" e "produtos_categorias" no MySQL com base no modelo fornecido.
9. **2 horas**: Escrever e testar as consultas SQL para as seguintes solicitações:
   - Listar produtos com preço superior a 100 reais.
   - Listar ids e preços de produtos com preço acima da média.
   - Calcular o preço médio dos produtos por categoria.
   
**Sprint 4: Inserções, Alterações e Remoções (3 horas)**

10. **1 hora**: Inserir pelo menos duas turmas diferentes na tabela "turma".
11. **1 hora**: Inserir pelo menos 1 aluno alocado em cada turma na tabela "aluno" (com "aluno_alocado" como NULL).
12. **1 hora**: Inserir pelo menos 2 alunos não alocados em nenhuma turma na tabela "aluno" (com "aluno_alocado" como NULL).

**Sprint 5: Atualização da Coluna "aluno_alocado" (2 horas)**

13. **2 horas**: Atualizar a coluna "aluno_alocado" na tabela "aluno" de acordo com as condições especificadas na etapa d.

**Revisão e Documentação (2 horas)**

14. **2 horas**: Revisar todo o trabalho realizado, garantindo que todas as partes funcionem conforme o esperado. Documentar o processo, incluindo qualquer problema encontrado e soluções implementadas.

**Entrega Final (15 horas no total)**

Vou explicar todas as etapas da sua avaliação, separando-as por tópicos e detalhando os requisitos e ações necessárias em cada uma delas.

**Modelagem e Normalização de Banco de Dados**

**Etapa 1: Modelo Conceitual (Commit 1)**
- Crie um modelo conceitual para o banco de dados, com base no esboço fornecido pelo gestor.
- Identifique os atributos-chave (colunas que representam identificadores únicos) nas tabelas "cliente" e "produto".
- Determine se existem atributos multivalorados (colunas que podem conter múltiplos valores) nas tabelas.
- Descreva a cardinalidade dos relacionamentos entre as tabelas "cliente" e "produto".

**Etapa 2: Modelo Lógico e Normalização (Commit 2)**
- Transforme o modelo conceitual em um modelo lógico, incluindo a definição das tabelas e suas chaves primárias.
- Decomponha os atributos multivalorados, se houver, para que as três primeiras formas normais sejam atendidas.
- Destaque as chaves primárias nas tabelas e descreva a cardinalidade dos relacionamentos entre elas.

**Consultas SQL em MySQL**

**Etapa 3: Consulta de Produtos Caros (Commit 3)**
- Escreva uma consulta SQL para listar os nomes de todos os produtos que custam mais de 100 reais.
- Ordene os resultados primeiro pelo preço e, em seguida, pelo nome.
- Use aliases para renomear as colunas "nome" como "Produto" e "preco" como "Valor".
- A resposta da consulta não deve incluir outras colunas de dados.

**Etapa 4: Consulta de Média de Preços (Commit 4)**
- Escreva uma consulta SQL para listar todos os ids e preços dos produtos cujo preço seja maior do que a média de todos os preços na tabela "produtos".

**Etapa 5: Consulta de Preço Médio por Categoria (Commit 5)**
- Escreva uma consulta SQL para calcular o preço médio dos produtos para cada categoria.
- Garanta que apenas as categorias com produtos associados apareçam no resultado.
- Ordene os resultados pelos nomes das categorias.

**Inserções, Alterações e Remoções em MySQL**

**Etapa 6: Criação do Banco de Dados Escola (Commit 6)**
- Utilize comandos DDL para criar as tabelas "aluno" e "turma" com suas colunas conforme especificado.
- Estabeleça a relação 1,n entre as entidades "aluno" e "turma" por meio da chave estrangeira "id_turma" na tabela "aluno".

**Etapa 7: Comandos DML (Commit 7)**
a) Inserir pelo menos duas turmas diferentes na tabela "turma".
b) Inserir pelo menos 1 aluno alocado em cada uma das turmas na tabela "aluno" (definindo "aluno_alocado" como NULL).
c) Inserir pelo menos 2 alunos não alocados em nenhuma turma na tabela "aluno" (com "aluno_alocado" como NULL).
d) Atualizar a coluna "aluno_alocado" na tabela "aluno" para que alunos associados a uma turma recebam o valor True e alunos não associados recebam o valor False.

Passo 1 -->>

**Modelo Conceitual:**

1. Abra o BRMODELO e crie um novo projeto.

2. Crie duas entidades: "Cliente" e "Produto". Para cada entidade, defina os atributos mencionados na descrição do projeto, ou seja, para "Cliente", você terá os atributos: "codigo_cliente", "nome_cliente", "sobrenome_cliente", "telefones_cliente", "municipio_cliente", "codigo_tipo_cliente" e "tipo_cliente". Para "Produto", terá os atributos: codigo_produto, nome_produto, descricao_produto, codigo_tipo_produto, tipo_produto, codigo_diretor_responsavel, nome_diretor_responsavel e email_diretor_responsavel.

3. Defina as chaves primárias para cada entidade. Por exemplo, "codigo_cliente" para "Cliente" e "codigo_produto" para "Produto".

4. Estabeleça o relacionamento entre as entidades "Cliente" e "Produto" conforme descrito na descrição do projeto. Um cliente pode estar associado a vários produtos, e um produto pode estar associado a vários clientes. Portanto, esse relacionamento é muitos-para-muitos. No BRMODELO, você pode representar isso criando um relacionamento "Muitos para Muitos" entre as duas entidades.

5. Destaque as cardinalidades nos relacionamentos. Por exemplo, "1..*" para "Cliente" e "1..*" para "Produto" para indicar que um cliente pode estar associado a vários produtos e vice-versa.

**Modelo Lógico:**

O modelo lógico será uma extensão do modelo conceitual, mas você precisará decompor atributos multivalorados, se existirem, e garantir que a estrutura atenda às três primeiras formas normais (1NF, 2NF e 3NF).

1. No BRMODELO, ajuste os atributos multivalorados, se houverem, decompondo-os em novas entidades conforme necessário para atender à normalização.

2. Certifique-se de que todas as entidades possuam chaves primárias definidas.

3. Atualize o relacionamento entre "Cliente" e "Produto" para refletir o novo modelo lógico, levando em consideração as decomposições necessárias.

4. Confirme que o modelo lógico está normalizado até a terceira forma normal.


1. **Arquitetura Cliente-Servidor**:
   - Continue a usar a arquitetura cliente-servidor com o MySQL como servidor de banco de dados e Python como cliente.

2. **ORM (Object-Relational Mapping)**:
   - O uso de uma biblioteca ORM como SQLAlchemy ainda pode ser benéfico para simplificar a interação com o banco de dados, mesmo em um ambiente de terminal ou Jupyter Notebook.

3. **API REST**:
   - Em vez de criar uma API REST, você pode criar scripts Python no Jupyter Notebook ou no terminal que interajam diretamente com o banco de dados usando a biblioteca MySQL Connector (ou outra biblioteca similar) para executar consultas SQL.

4. **Controle de Acesso**:
   - Mantenha a segurança e a privacidade dos dados, mesmo em um ambiente de terminal ou notebook. Use autenticação e autorização para proteger o acesso ao banco de dados.

5. **Indexação e Otimização**:
   - Continue a otimizar suas consultas SQL e a estrutura do banco de dados para obter um desempenho eficiente.

6. **Cache**:
   - Dependendo das necessidades de desempenho, você ainda pode considerar o uso de cache em seu código Python para armazenar em cache resultados de consultas frequentes.

7. **Escalabilidade**:
   - Embora você possa não precisar de escalabilidade em um ambiente de terminal ou notebook, ainda é uma boa prática planejar a estrutura do banco de dados e do código Python para facilitar futuras expansões.

8. **Monitoramento e Logging**:
   - Implemente ferramentas de monitoramento e logging em seu código Python para rastrear o desempenho e identificar problemas.

9. **Backup e Recuperação**:
   - Mantenha rotinas de backup e recuperação para proteger seus dados.

10. **Documentação**:
    - A documentação detalhada do esquema do banco de dados e a estrutura das consultas SQL continuam sendo importantes para facilitar o desenvolvimento e a manutenção.