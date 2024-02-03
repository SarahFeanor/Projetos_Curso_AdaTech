```markdown
# Tutorial MySQL Básico para Iniciantes (Linux Mint)

## Instalação do MySQL no Linux Mint:

1. **Abra um terminal:** Pressione `Ctrl + Alt + T` para abrir um terminal.

2. **Atualize os pacotes:** Execute o seguinte comando para atualizar seus pacotes:

   ```
   sudo apt update
   sudo apt upgrade
   ```

3. **Instale o MySQL Server:** Use o seguinte comando para instalar o servidor MySQL:

   ```
   sudo apt install mysql-server
   ```

4. **Inicie o MySQL Server:** Inicie o serviço do MySQL com o seguinte comando:

   ```
   sudo service mysql start
   ```

5. **Configure o MySQL:** Execute o seguinte comando para configurar a segurança do MySQL:

   ```
   sudo mysql_secure_installation
   ```

   Siga as instruções para definir a senha do root e responder às perguntas de segurança.

## Conectando e Criando um Banco de Dados:

1. **Conectando ao MySQL:** Use o seguinte comando para se conectar ao MySQL como usuário root:

   ```
   mysql -u root -p
   ```

   Insira a senha que você configurou durante a instalação.

2. **Criando um Banco de Dados:** Após se conectar, crie um banco de dados com este comando:

   ```
   CREATE DATABASE nomedoBanco;
   ```

   Substitua "nomedoBanco" pelo nome desejado para o banco de dados.

3. **Usando o Banco de Dados:** Para começar a usar o banco de dados criado, digite:

   ```
   USE nomedoBanco;
   ```

## Criando uma Tabela e Inserindo Dados Mock:

1. **Criando uma Tabela:** Vamos criar uma tabela para armazenar informações fictícias de usuários:

   ```
   CREATE TABLE usuarios (
       id INT AUTO_INCREMENT PRIMARY KEY,
       nome VARCHAR(50),
       email VARCHAR(50)
   );
   ```

2. **Inserindo Dados:** Insira dados fictícios na tabela:

   ```
   INSERT INTO usuarios (nome, email)
   VALUES
       ('João', 'joao@example.com'),
       ('Maria', 'maria@example.com'),
       ('Pedro', 'pedro@example.com');
   ```

3. **Recuperando Dados:** Para verificar se os dados foram inseridos corretamente:

   ```
   SELECT * FROM usuarios;
   ```

## Possíveis Problemas e Soluções:

- **Erro de senha do MySQL:** Se esquecer a senha do root do MySQL, siga as instruções do MySQL para redefinir a senha.

- **Erro de permissão negada:** Verifique se está usando o usuário root ou tem permissões adequadas para criar bancos de dados e tabelas.

- **Erro de porta em uso:** Verifique se outra instância do MySQL está usando a mesma porta.

- **Erro de sintaxe:** Revise seus comandos para evitar erros de digitação.

Lembre-se de praticar para se familiarizar mais com o MySQL.
```

docker run --name database --rm -e MYSQL_ROOT_PASSWORD=123456 -p 3306:3306 --network host mysql:8.0-debian


