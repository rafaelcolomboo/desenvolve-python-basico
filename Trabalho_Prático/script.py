import csv

# Dicionário para armazenar os usuários (nome -> (senha, permissão))
usuarios = {}

# Dicionário para armazenar os produtos (código -> {'nome', 'preço', 'quantidade'})
produtos = {}

# Carregar usuários do arquivo usuarios.csv
def carregar_usuarios():
    with open('usuarios.csv', 'r', newline='') as arquivo:
        leitor_csv = csv.reader(arquivo)
        for linha in leitor_csv:
            nome_usuario, senha, permissao = linha
            usuarios[nome_usuario] = (senha, int(permissao))

# Salvar usuários no arquivo usuarios.csv
def salvar_usuarios():
    with open('usuarios.csv', 'w', newline='') as arquivo:
        escritor_csv = csv.writer(arquivo)
        for nome_usuario, (senha, permissao) in usuarios.items():
            escritor_csv.writerow([nome_usuario, senha, permissao])

# Carregar produtos do arquivo produtos.csv
def carregar_produtos():
    with open('produtos.csv', 'r', newline='') as arquivo:
        leitor_csv = csv.DictReader(arquivo)
        for linha in leitor_csv:
            codigo = linha['codigo']
            produtos[codigo] = {
                'nome': linha['nome'],
                'preco': float(linha['preco']),
                'quantidade': int(linha['quantidade'])
            }

# Salvar produtos no arquivo produtos.csv
def salvar_produtos():
    with open('produtos.csv', 'w', newline='') as arquivo:
        campos = ['codigo', 'nome', 'preco', 'quantidade']
        escritor_csv = csv.DictWriter(arquivo, fieldnames=campos)
        escritor_csv.writeheader()
        for codigo, produto in produtos.items():
            produto['codigo'] = codigo  # Garantir que o código seja salvo como chave
            escritor_csv.writerow(produto)

# Função para adicionar novo usuário (C do CRUD)
def adicionar_usuario(nome_usuario, senha, permissao):
    usuarios[nome_usuario] = (senha, permissao)
    salvar_usuarios()

# Função para listar todos os usuários (R do CRUD)
def listar_usuarios():
    for nome_usuario, (senha, permissao) in usuarios.items():
        print(f"Usuário: {nome_usuario} | Permissão: {permissao}")

# Função para atualizar senha de um usuário (U do CRUD)
def atualizar_senha_usuario(nome_usuario, nova_senha):
    if nome_usuario in usuarios:
        senha_atual, permissao = usuarios[nome_usuario]
        usuarios[nome_usuario] = (nova_senha, permissao)
        salvar_usuarios()
        print(f"Senha do usuário {nome_usuario} atualizada com sucesso.")

# Função para remover usuário (D do CRUD)
def remover_usuario(nome_usuario):
    if nome_usuario in usuarios:
        del usuarios[nome_usuario]
        salvar_usuarios()
        print(f"Usuário {nome_usuario} removido com sucesso.")

# Função para adicionar novo produto (C do CRUD)
def adicionar_produto(codigo, nome, preco, quantidade):
    produtos[codigo] = {'nome': nome, 'preco': preco, 'quantidade': quantidade}
    salvar_produtos()

# Função para listar todos os produtos (R do CRUD)
def listar_produtos():
    for codigo, produto in produtos.items():
        print(f"Código: {codigo} | Nome: {produto['nome']} | Preço: R${produto['preco']} | Quantidade: {produto['quantidade']}")

# Função para atualizar preço ou quantidade de um produto (U do CRUD)
def atualizar_produto(codigo, novo_preco=None, nova_quantidade=None):
    if codigo in produtos:
        if novo_preco is not None:
            produtos[codigo]['preco'] = novo_preco
        if nova_quantidade is not None:
            produtos[codigo]['quantidade'] = nova_quantidade
        salvar_produtos()
        print(f"Produto {codigo} atualizado com sucesso.")

# Função para remover produto (D do CRUD)
def remover_produto(codigo):
    if codigo in produtos:
        del produtos[codigo]
        salvar_produtos()
        print(f"Produto {codigo} removido com sucesso.")

# Função para buscar produto por código
def buscar_produto(codigo):
    if codigo in produtos:
        print(f"Produto encontrado - Código: {codigo} | Nome: {produtos[codigo]['nome']} | Preço: R${produtos[codigo]['preco']} | Quantidade: {produtos[codigo]['quantidade']}")
    else:
        print(f"Produto com código {codigo} não encontrado.")

# Função para imprimir produtos ordenados por nome
def imprimir_produtos_ordem_nome():
    produtos_ordenados = sorted(produtos.items(), key=lambda x: x[1]['nome'])
    for codigo, produto in produtos_ordenados:
        print(f"Código: {codigo} | Nome: {produto['nome']} | Preço: R${produto['preco']} | Quantidade: {produto['quantidade']}")

# Função para imprimir produtos ordenados por preço
def imprimir_produtos_ordem_preco():
    produtos_ordenados = sorted(produtos.items(), key=lambda x: x[1]['preco'])
    for codigo, produto in produtos_ordenados:
        print(f"Código: {codigo} | Nome: {produto['nome']} | Preço: R${produto['preco']} | Quantidade: {produto['quantidade']}")

# Exemplo de uso do sistema

# Carregar dados dos arquivos
carregar_usuarios()
carregar_produtos()

# Adicionar usuários
adicionar_usuario('gerente', 'senha123', 1)
adicionar_usuario('funcionario', 'abc123', 2)
adicionar_usuario('cliente', 'cliente123', 3)

# Listar usuários
print("=== Lista de Usuários ===")
listar_usuarios()
print()

# Atualizar senha de um usuário
atualizar_senha_usuario('funcionario', 'nova123')

# Remover um usuário
remover_usuario('cliente')

# Adicionar produtos
adicionar_produto('001', 'Smartphone', 1500.00, 10)
adicionar_produto('002', 'Notebook', 3000.00, 5)
adicionar_produto('003', 'Tablet', 800.00, 8)

# Listar produtos
print("\n=== Lista de Produtos ===")
listar_produtos()
print()

# Atualizar preço de um produto
atualizar_produto('001', 1600.00)

# Buscar produto por código
print("\n=== Buscar Produto ===")
buscar_produto('002')
buscar_produto('004')

# Imprimir produtos ordenados por nome
print("\n=== Produtos Ordenados por Nome ===")
imprimir_produtos_ordem_nome()

# Imprimir produtos ordenados por preço
print
