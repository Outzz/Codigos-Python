CREATE TABLE avaliacao(
  id INT PRIMARY KEY,
  estrelas INT(1),
  comentario VARCHAR(500),
  dispositivo VARCHAR(8)
  );
  
  CREATE TABLE produtos (
  id INT PRIMARY KEY,
  nome_produto VARCHAR(150),
  quantidade INT,
  tipo VARCHAR(100),
  fornecedor VARCHAR(200)
  );
  
  CREATE TABLE usuarios (
  id INT PRIMARY KEY,
  nome VARCHAR(100),
  idade INT,
  telefone VARCHAR(17),
  senha TEXT(150)
  );
  
  CREATE TABLE forma_de_pagamento(
  id INT PRIMARY KEY,
  pagamento VARCHAR(7),
  VEZES INT(12),
  data DATE
  );
  
  INSERT INTO usuarios(id, nome, idade, telefone)
  VALUES
  (1, 'Joao', 26, 1399999999);
  
  SELECT * FROM usuarios;
