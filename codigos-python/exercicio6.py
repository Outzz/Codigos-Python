import datetime
from decimal import Decimal
import sqlite3
import pandas as pd
from dataclasses import dataclass
from typing import List, Dict

@dataclass
class Cliente:
    nome: str
    email: str
    numero: str

clientes = []

@dataclass 
class Servico:
    nome: str
    valor: Decimal

servicos = []

@dataclass
class Peca:
    nome: str
    preco_custo: Decimal
    quantidade: int

pecas = []
estoque = []

def criar_cliente():
    nome = input("Nome do cliente: ")
    email = input("Email do cliente: ")
    numero = input("Número do cliente: ")
    cliente = Cliente(nome, email, numero)
    clientes.append(cliente)
    print(f"Cliente cadastrado com sucesso😎")

def cadastrar_servico():
    nome = input("Nome do serviço: ")
    valor = Decimal(input("Valor do serviço (R$): "))
    servico = Servico(nome, valor)
    servicos.append(servico)
    print(f"Serviço {nome} cadastrado com sucesso!")

def listar_estoque():
    print("\n--- 📦 ESTOQUE ---")
    for p in estoque:
        print(f"{p.nome:<20} | Custo: R${p.preco_custo:.2f} | Qtd: {p.quantidade}")

def cadastrar_peca():
    nome = input("Nome da peça: ")
    preco = Decimal(input("Preço de custo (R$): "))
    qtd = int(input("Quantidade inicial no estoque: "))
    peca = Peca(nome, preco, qtd)
    pecas.append(peca)
    print(f"Peça {nome} cadastrada com {qtd} unidades.")

def gerar_orcamento():
    if not clientes:
        print("Nenhum cliente cadastrado😥")
        return
    
    cliente = clientes[-1]
    data = datetime.date.today().strftime("%d/%m/%Y")
    print("\n==== ORÇAMENTO TECHFIX ====")
    print(f"Cliente: {cliente.nome}")
    print(f"Data: {data}\n")

    total_servicos = sum(s.valor for s in servicos)
    print("Serviços:")
    for s in servicos:
        print(f"- {s.nome:<20} R$ {s.valor:.2f}")

    print("\nPeças:")
    total_pecas = Decimal("0.00")
    for p in pecas:
        if p.quantidade > 0:
            mao_obra = p.preco_custo * Decimal("0.30")
            preco_final = p.preco_custo + mao_obra
            total_pecas += preco_final
            print(f"- {p.nome:<20} Custo: R$ {p.preco_custo:.2f} | Final: R$ {preco_final:.2f}")

    total_final = total_servicos + total_pecas
    print("\n-----------------------------------")
    print(f"TOTAL: R$ {total_final:.2f}")
    print("\nObs: Caso não aprove, será cobrada taxa de R$30,00.")
    print("Após 30 dias do prazo, taxa de R$10/dia.")

def menu():
    print("\n====== 🛠️ TechFix 🛠️ ======")
    print("1 - Cadastrar Cliente")
    print("2 - Cadastrar Serviço")
    print("3 - Cadastrar Peça")
    print("4 - Gerar Orçamento")
    print("5 -  Sair")
    return input("Escolha o que irá fazer: ")

while True:
    opcao = menu()
    if opcao == "1":
        criar_cliente()
    elif opcao == "2":
        cadastrar_servico()
    elif opcao == "3":
        cadastrar_peca()
    elif opcao == "4":
        gerar_orcamento()
    elif opcao == "5":
        print("Saindo... Até logo!")
        break
    else:
        print("Opção inválida, tente novamente.")
    
