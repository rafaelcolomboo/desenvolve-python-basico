# Dados dos livros
livros = [
    ["O Senhor dos Anéis: A Sociedade do Anel", "J.R.R. Tolkien", 1954, 423],
    ["O Alquimista", "Paulo Coelho", 1988, 208],
    ["O Apanhador no Campo de Centeio", "J.D. Salinger", 1951, 214],
    ["Uma terra prometida", "Barack Obama", 2020, 768],
    ["Orgulho e Preconceito", "Jane Austen", 1813, 279],
    ["Cidade de Deus", "Paulo Lins", 1997, 592],
    ["O Drible", "Sérgio Rodrigues", 2013, 288],
    ["A Culpa é das Estrelas", "John Green", 2012, 313],
    ["Guerra e Paz", "Leo Tolstoy", 1869, 1225],
    ["O Pequeno Príncipe", "Antoine de Saint-Exupéry", 1943, 96]
]

# Cria o arquivo CSV
with open("meus_livros.csv", "w", encoding="utf-8") as file:
    # Escreve a primeira linha com os títulos das colunas
    file.write("Título,Autor,Ano de publicação,Número de páginas\n")
    
    # Escreve os dados dos livros
    for livro in livros:
        file.write(",".join(map(str, livro)) + "\n")
        
print("Arquivo 'meus_livros.csv' criado com sucesso.")
