produtos = []
carrinho = []

def menu():
    print("\n===== MINI MERCADO LIVRE =====")
    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Pesquisar produto")
    print("4 - Adicionar ao carrinho")
    print("5 - Ver carrinho")
    print("6 - Finalizar compra")
    print("7 - Avaliar produto")
    print("0 - Sair")
    return input("Escolha uma opção: ")

def cadastrar_produto():
    nome = input("Nome do produto: ")
    preco = float(input("Preço: R$ "))
    estoque = int(input("Quantidade em estoque: "))

    produto = {
        "nome": nome,
        "preco": preco,
        "estoque": estoque,
        "avaliacoes": []
    }

    produtos.append(produto)
    print("✅ Produto cadastrado!")

def listar_produtos():
    if len(produtos) == 0:
        print("❌ Nenhum produto disponível.")
        return

    print("\n--- PRODUTOS DISPONÍVEIS ---")
    for i, p in enumerate(produtos):
        if len(p["avaliacoes"]) > 0:
            media = sum(p["avaliacoes"]) / len(p["avaliacoes"])
        else:
            media = 0

        print(f"{i} - {p['nome']} | R$ {p['preco']} | Estoque: {p['estoque']} | ⭐ {media:.1f}")

def pesquisar_produto():
    termo = input("Digite o nome do produto: ").lower()

    for i, p in enumerate(produtos):
        if termo in p["nome"].lower():
            print(f"{i} - {p['nome']} | R$ {p['preco']} | Estoque: {p['estoque']}")

def adicionar_carrinho():
    listar_produtos()
    if len(produtos) == 0:
        return

    indice = int(input("Digite o número do produto: "))
    quantidade = int(input("Quantidade: "))

    produto = produtos[indice]

    if quantidade <= produto["estoque"]:
        carrinho.append({
            "nome": produto["nome"],
            "preco": produto["preco"],
            "quantidade": quantidade
        })
        produto["estoque"] -= quantidade
        print("🛒 Produto adicionado ao carrinho!")
    else:
        print("❌ Estoque insuficiente.")

def ver_carrinho():
    if len(carrinho) == 0:
        print("🛒❌ Carrinho vazio.")
        return

    total = 0
    print("\n--- CARRINHO ---")
    for item in carrinho:
        subtotal = item["preco"] * item["quantidade"]
        total += subtotal
        print(f"{item['nome']} | {item['quantidade']}x | R$ {subtotal}")

    print(f"💰 Total: R$ {total}")

def finalizar_compra():
    if len(carrinho) == 0:
        print("❌ Carrinho vazio.")
        return

    ver_carrinho()
    confirmar = input("Confirmar compra? (s/n): ")

    if confirmar.lower() == "s":
        carrinho.clear()
        print("✅ Compra realizada com sucesso!")
    else:
        print("❌ Compra cancelada.")

def avaliar_produto():
    listar_produtos()
    if len(produtos) == 0:
        return

    indice = int(input("Digite o número do produto: "))
    nota = int(input("Nota (1 a 5): "))

    if 1 <= nota <= 5:
        produtos[indice]["avaliacoes"].append(nota)
        print("⭐ Avaliação registrada!")
    else:
        print("❌ Nota inválida.")

while True:
    opcao = menu()

    if opcao == "1":
        cadastrar_produto()
    elif opcao == "2":
        listar_produtos()
    elif opcao == "3":
        pesquisar_produto()
    elif opcao == "4":
        adicionar_carrinho()
    elif opcao == "5":
        ver_carrinho()
    elif opcao == "6":
        finalizar_compra()
    elif opcao == "7":
        avaliar_produto()
    elif opcao == "0":
        print("👋 Saindo do sistema...")
        break
    else:
        print("Opção inválida.")
