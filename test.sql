CREATE TABLE avaliacao(
  id INT PRIMARY KEY,
  estrelas INT(1),
  dispositivo VARCHAR(8)
  );
  
  CREATE TABLE produtos (
  id INT PRIMARY KEY,
  nome VARCHAR(150),
  preco DECIMAL(10, 2),
  estoque INT,
  data_cadastro DATE,
  categoria VARCHAR(200)
  );
  
  CREATE TABLE usuarios (
  id INT PRIMARY KEY,
  nome VARCHAR(100),
  idade INT,
  telefone VARCHAR(17),
  senha VARCHAR(150)
  );
  
  CREATE TABLE forma_de_pagamento(
  id INT PRIMARY KEY,
  pagamento VARCHAR(20),
  VEZES INT,
  data DATE
  );
  
  CREATE TABLE compras(
  id INT PRIMARY KEY,
  id_usuario INT,
  id_produto INT,
  id_pagamento INT,
  quantidade INT,
  valor_total DECIMAL(10,2),
  data_compra DATE
  );
  ALTER TABLE compras
  ADD status VARCHAR(30)
  UPDATE compras
  Set status = 'Aguardando Pagamento'
  AND data_compra BETWEEN '2026-02-01' ANd '2026-02-28';
  
  INSERT INTO produtos(id, nome, categoria, preco, estoque)
  VALUES
  (1, 'Batata frita congelada', 'Comida', 3000.00, 100),
  (2, 'Hamburguer artesanal congelado', 'Comida', 250.50, 80),
  (3, 'Refrigerante Cola 2L', 'Bebida', 19.99, 200),
  (4, 'Suco de Laranja Natural', 'Bebida', 102.00, 60),
  (5, 'Chocolate ao leite 90g', 'Doce', 68.50, 150),
  (6, 'Biscoito recheado', 'Doce', 200.75, 120),
  (7, 'Pizza congelada Calabresa', 'Comida', 78.90, 70),
  (8, 'Sorvete Napolitano 1L', 'Sobremesa', 42.00, 50),
  (9, 'Água mineral 500ml', 'Bebida', 29.50, 300),
  (10, 'Café torrado e moído 500g', 'Mercearia', 1600.80, 90);
  
  SELECT * FROM produtos
  WHERE preco > 50.00;
  
  SELECT * FROM produtos
  WHERE estoque < 5;
  
  SELECT * FROM produtos
  WHERE preco BETWEEN 100 AND 500
  AND estoque > 0;
  SELECT * FROM avaliacao
  WHERE estrelas < 3;
  
 
