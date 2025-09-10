from dataclasses import dataclass
from datetime import datetime

@dataclass
class Usuario:
    nome: str
    email: str
    senha: str

@dataclass
class Publicacao:
    conteudo: str
    descricao: str
    autor: str
    data_hora: datetime
    curtidas: int = 0
    comentarios: list = None 

    def __post_init__(self):
        if self.comentarios is None:
            self.comentarios = []

@dataclass
class Comentario:
    autor: str
    conteudo: str
    data_hora: datetime

lista_usuarios = []
lista_publicacoes = []

def criar_usuario():
    nome = input("Qual o seu nome: ")
    email = input("Qual o seu email: ")
    senha = input("Qual a sua senha: ")
    usuario_digitado = Usuario(nome,email,senha)
    lista_usuarios.append(usuario_digitado)
    print("Cadastro efetuado com sucesso")

def pesquisar_email():
    nome_digitado = input("Qual o seu nome: ")
    for usuario in lista_usuarios:
        if usuario.nome == nome_digitado:
            print(f"email desse usuario -> {usuario.email}")
            
def fazer_login():
    login_email = input("Qual o seu email: ")
    login_senha = input("Qual a sua senha: ")
        
    for usuario in lista_usuarios:
        if usuario.email == login_email and usuario.senha == login_senha:
            print("Acesso autorizado")
            return usuario  # ✅ Retorna o usuário logado

    print("Email ou senha incorreto")
    return None  # ❌ Login falhou

def criar_publicacao(usuario_logado):
    print("\n === Criar Publicação ===")
    conteudo = input("Digite a publicação: ")
    descricao = input("Descrição: ")
    nova_publicacao = Publicacao(
        conteudo,
        descricao,
        autor=usuario_logado.nome,
        data_hora=datetime.now()
    )
    lista_publicacoes.append(nova_publicacao)
    print("Publicação postada!")

def comentar_publicacao(usuario_logado):
    if not lista_publicacoes:
        print("Nenhuma publicação disponível para comentar😢")
        return

    print("\n=== Publicações Disponíveis ===")
    for i, pub in enumerate(lista_publicacoes):
        print(f"{i} - {pub.descricao} (Autor: {pub.autor})")

    try:
        indice = int(input("Digite o número da publicação que você quer comentar: "))
        if 0 <= indice < len(lista_publicacoes):
            texto = input("Digite o seu comentário: ")
            novo_comentario = Comentario(
                autor=usuario_logado.nome,
                conteudo=texto,
                data_hora=datetime.now()
            )
            lista_publicacoes[indice].comentarios.append(novo_comentario)
            print("Comentário Adicionado Com Sucesso!")
        else:
            print("Comentário inválido. Tente novamente")
    except ValueError:
        print("Digite um número válido!")

        
def mostrar_menu():
    print("\n === Bem-Vindo! O que deseja fazer? ===")
    print("1 - Cadastro")
    print("2 - Login")
    print("3 - Buscar usuário com email")
    print("4 - Fazer publicação")
    print("5 - Ver publicações")
    print("6 - Curtir publicações")
    print("7 - Comentar Publicação")
    print("0 - Sair")
    return input("Digite a opção: ")
    
# controla o usuário logado
usuario_atual = None

while True:
    opcao = mostrar_menu()

    if opcao == "1":
        criar_usuario()

    elif opcao == "2":
        usuario_atual = fazer_login()

    elif opcao == "3":
        pesquisar_email()

    elif opcao == "4":
        if usuario_atual:
            criar_publicacao(usuario_atual)
        else:
            print("Você precisa estar logado para fazer uma publicação.")

    elif opcao == "5":
        print("\n=== Publicações ===")
        if not lista_publicacoes:
            print("Nenhuma publicação encontrada.")
        for pub in lista_publicacoes:
            print(f"\nAutor: {pub.autor}")
            print(f"Conteúdo: {pub.conteudo}")
            print(f"Descrição: {pub.descricao}")
            print(f"Data/Hora: {pub.data_hora.strftime('%d/%m/%Y %H:%M:%S')}")
            print(f"Curtidas: {pub.curtidas}")
            print(f"Comentários:")
            if pub.comentarios:
                for comentario in pub.comentarios:
                    print(f" - {comentario.autor} ({comentario.data_hora.strftime('%d/%m %H:%M')}): {comentario.conteudo}")
                else:
                    print("Nenhum comentário ainda.")
            
    elif opcao == "6":
        print("\n=== Curtir Publicação ===")
        if not lista_publicacoes:
            print("Nenhuma publicação disponível para curtir.")
            continue
    
        for i, pub in enumerate(lista_publicacoes):
            print(f"{i} - {pub.descricao} (Autor: {pub.autor}, Curtidas: {pub.curtidas})")
    
        try:
            indice = int(input("Digite o número da publicação que deseja curtir: "))
            if 0 <= indice < len(lista_publicacoes):
                lista_publicacoes[indice].curtidas += 1
                print("Você curtiu a publicação!")
            else:
                print("Índice inválido.")
        except ValueError:
            print("Por favor, digite um número válido.")

    elif opcao == "7":
        if usuario_atual:
            comentar_publicacao(usuario_atual)
        else:
            print("Você precisa estar logado para comentar.")

    elif opcao == "0":
        print("Encerrando o programa.")
        break
