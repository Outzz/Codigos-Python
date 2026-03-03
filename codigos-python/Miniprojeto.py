from dataclasses import dataclass
from datetime import datetime

@dataclass
class Fornecedor:
    id: int
    nome_empresa: str
    cnpj: str
    
@dataclass
class Produto:
    id: int
    nome: str
    categoria: str
    tamanho: str
    cor: str
    codigo_barras: str
    valor_custo: float
    valor_venda: float
    estoque: int
    fornecedor_id: int
    
@dataclass
class MovimentoEstoque:
    id: int
    produto_id: int
    tipo: str
    quantidade: int
    data_hora: str
    
@dataclass
class Compra:
    id: int
    produto_id: int
    quantidade: int
    total: float
    data_hora: int
    
fornecedores = []
produtos = []
movimentos = []
compras = []

def proximo_id(lista):
    return len(lista) + 1
    
def agora():
    return datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    
def cadastrar_fornecedor():
    print("\n----- CADASTRO DE FORNECEDOR -----")
    nome = input("Digite o nome da empresa: ")
    cnpj = input("Digite seu CNPJ: ")
    
    fornecedor = Fornecedor(
        proximo_id(fornecedores),
        nome,
        cnpj
        )
        
    fornecedores.append(fornecedor)
    print("Fornecedor Cadastrado com Sucesso🚀")
    
    
def listar_fornecedores():
    for f in fornecedores:
        print(f)
        
def cadastrar_produtos():
    if len(fornecedores) == 0:
        print("Cadastre um fornecedor primeiro")
        return
    
    print("\n----- Cadastrar Produtos -----")
    nome = input("NOME: ")
    categoria = input("CATEGORIA: ")
    tamanho = input("TAMANHO: ")
    cor = input("COR: ")
    codigo_barras = input("CÓDIGO DE BARRAS: ")
    custo = float(input("CUSTO: "))
    venda = float(input("VENDA: "))
    estoque = int(input("ESTOQUE: "))
    
    print("\nFORNECEDORES:")
    listar_fornecedores()
    fornecedor_id = int(input("ID DO FORNECEDOR: "))
    
    produto = Produto(
        proximo_id(produtos),
        nome,
        categoria, 
        tamanho,
        cor,
        codigo_barras,
        custo,
        venda,
        estoque,
        fornecedor_id
    )

    produtos.append(produto)
    
    if estoque > 0:
        movimento = MovimentoEstoque(
            proximo_id(movimento),
            produto.id,
            "ENTRADA",
            estoque,
            agora()
        )
        
        movimentos.append(movimento)
    
    print("PRODUTO CADASTRADO COM SUCESSO🚀")
    
def listar_produtos():
    print("\n----- PRODUTOS -----")
    for p in produtos:
        print(p)
    
def entrada_estoque():
    print("\n----- ENTRADA DE ESTOQUE -----")
    listar_produtos()
    
    pid = int(input("ID do Produto: "))
    quantidade = int(input("Quantidade: "))
    
    for p in produtos:
        if p.id == pid:
            p.estoque += quantidade
            
            movimento = MovimentoEstoque(
            proximo_id(movimentos),
            pid,
            "ENTRADA",
            quantidade,
            agora()
        )
        movimentos.append(movimento)
        
        print("Entrada Registrada🚀")
        
def saida_estoque(tipo):
    print("\n----- SAÍDA ESTOQUE -----")
    listar_produtos()
    
    pid = int(input("ID do Produto: "))
    quantidade = int(input("Quantidade: "))
    
    for p in produtos:
        if p.id == pid:
            if quantidade <= p.estoque:
                p.estoque -= p.quantidade
                
                movimento = MovimentoEstoque(
                proximo_id(movimentos),
                pid,
                tipo,
                quantidade,
                agora()
            )
            movimentos.append(movimento)
            
            print("Saída Registrada")
        else:
            print("Estoque Insuficiente❌")
            
def comprar():
    print("\n----- COMPRA -----")
    listar_compras()
    
    pid = int(input("ID do Produto: "))
    quantidade = int(input("Quantidade: "))
    
    for p in produtos:
        if p.id == pid:
            if quantidade <= p.estoque:
                p.estoque -= p.quantidade
                
                total = p.valor_venda * quantidade
                
                compra = Compra(
                    proximo_id(movimentos),
                    pid,
                    quantidade,
                    total,
                    agora()
                    )
                compras.append(compra)
                
                movimento = MovimentoEstoque(
                proximo_id(movimentos),
                pid,
                "SAÍDA VENDA",
                quantidade,
                agora()
            )
            movimentos.append(movimento)
            
            print("Compra Realizada! Total: ", total)

def listar_compras():
    print("\n----- COMPRAS -----")
    for c in compras:
     print(c)
     
def listar_movimentos():
    print("\n----- MOVIMENTO -----")
    for m in movimentos:
        print(m)

def menu():
    while True:
        print("\n ----- Menu Inicial -----")
        print("1 - Cadastrar fornecedor")
        print("2 - Cadastrar produto")
        print("3 - Entrada de estoque")
        print("4 - Saída por venda")
        print("5 - Cadastrar fornecedor")
        print("6 - Saída por avaria")
        print("7 - Comprar produto")
        print("8 - Listar produtos")
        print("9 - Listar compras")
        print("10 - Listar movimentos")
        print("0 - Sair")

        op = input("Escolha: ")

        if op == "1":
            cadastrar_fornecedor()
        elif op == "2":
            cadastrar_produtos()
        elif op == "3":
            entrada_estoque()
        elif op == "4":
            saida_estoque("SAIDA_VENDA")
        elif op == "5":
            saida_estoque("SAIDA_TROCA")
        elif op == "6":
            saida_estoque("SAIDA_AVARIA")
        elif op == "7":
            comprar()
        elif op == "8":
            listar_produtos()
        elif op == "9":
            listar_compras()
        elif op == "10":
            listar_movimentos()
        elif op == "0":
            break
        else:
            print("Opção inválida.")



menu()
