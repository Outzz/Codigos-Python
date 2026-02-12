CREATE TABLE avaliacao(
  id INT PRIMARY KEY,
  estrelas INT,
  comentario VARCHAR
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
  senha VARCHAR(150),
  email VARCHAR(100)
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
  data_compra DATE,
  status VARCHAR(30)
  );
  
  UPDATE compras
  Set status = 'Aguardando Pagamento'
  WHERE data_compra BETWEEN '2026-02-01' ANd '2026-02-28';
  
  UPDATE produto
  SET estoque = estoque + 7
  WHERE id = 1;
  
  UPDATE produto
  SET preco = preco * 1.1;
  
  UPDATE usuario
  SET email = 'joaosilva10@gmail.com'
  WHERE id = 1;
  
  UPDATE compras
  SET status = 'Entregue'
  WHERE id = 1;
  
  UPDATE produtos
  SET estoque = estoque - 1
  WHERE estoque > 5;
  
  UPDATE produtos
  SET preco = preco * 0.8
  WHERE preco < 1000;
  
  INSERT INTO produtos(id, nome, categoria, preco, estoque)
  VALUES
  (1, 'Batata frita congelada', 'Comida', 3000.00, 100),
  (2, 'Hamburguer artesanal congelado', 'Comida', 250.50, 80),
  (3, 'Refrigerante Cola 2L', 'Bebida', 19.99, 200),
  (4, 'Suco de Laranja Natural', 'Bebida', 102.00, 60),
  (5, 'Chocolate ao leite 90g', 'Doce', 68.50, 150);
  
  INSERT INTO usuarios (id, nome, idade, telefone, senha, email)
  VALUES
  (1, 'João Silva', 25, '(11)99999-1111', 'senha123', 'joaosilva@gmail.com'),
  (2, 'Maria Souza', 30, '(11)98888-2222', 'maria456', 'mariasouza@gmail.com'),
  (3, 'Carlos Lima', 22, '(11)97777-3333', 'carlos789', 'carloslima@gmail.com'),
  (4, 'Ana Oliveira', 28, '(11)96666-4444', 'ana321', 'anaoliveira@gmail.com'),
  (5, 'Fernanda Costa', 35, '(11)95555-5555', 'fernanda654', 'fernandacosta@gmail.com');
  
  INSERT INTO forma_de_pagamento (id, pagamento, VEZES, data)
  VALUES
  (1, 'Cartão de Crédito', 3, '2026-02-05'),
  (2, 'Pix', 1, '2026-02-10'),
  (3, 'Boleto', 1, '2026-02-15'),
  (4, 'Cartão de Crédito', 5, '2026-02-20'),
  (5, 'Débito', 1, '2026-02-25');
  
  INSERT INTO compras (id, id_usuario, id_produto, id_pagamento, quantidade, valor_total, data_compra, status)
  VALUES
  (1, 1, 3, 1, 2, 39.98, '2026-02-05', 'Aguardando Pagamento'),
  (2, 2, 5, 2, 1, 68.50, '2026-02-10', 'Pago'),
  (3, 3, 1, 3, 3, 9000.00, '2026-02-12', 'Aguardando Pagamento'),
  (4, 4, 8, 4, 2, 84.00, '2026-02-18', 'Enviado'),
  (5, 5, 2, 5, 1, 250.50, '2026-02-22', 'Entregue');
  
  INSERT INTO avaliacao (id, estrelas, comentario)
  VALUES
  (1, 5, 'Produto excelente, chegou rápido!'),
  (2, 2, 'Demorou muito para entregar.'),
  (3, 4, 'Muito bom, recomendo.'),
  (4, 1, 'Produto veio com defeito.'),
  (5, 3, 'Bom, mas pode melhorar.');
  
  SELECT * FROM produtos
  WHERE preco > 50.00 AND estoque < 5;
  
  SELECT * FROM produtos
  WHERE preco BETWEEN 100 AND 500
  AND estoque > 0;
  SELECT * FROM avaliacao
  WHERE estrelas < 3;
  
  SELECT * FROM compras;
  
  SELECT * FROM usuarios;
  
  SELECT * FROM forma_de_pagamento;
