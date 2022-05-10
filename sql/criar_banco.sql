-- Dropar tabelas se elas existirem
DROP TABLE IF EXISTS tarefas;

-- Criar banco
CREATE TABLE tarefas (
    id INT GENERATED ALWAYS AS IDENTITY, 
    descricao VARCHAR(250),
    situacao VARCHAR(250), 
    PRIMARY KEY (id)
    );
