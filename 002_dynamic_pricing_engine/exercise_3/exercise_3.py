# ==================================================================================================
# 70. Processamento de produtos com contexto (e-commerce)
# ==================================================================================================
#
# O sistema da loja deixou de trabalhar apenas com preços.
#
# Agora cada produto possui:
#
# - nome
# - categoria
# - preço
#
# Dados:
#
# produtos = [
#     ('Notebook', 'tecnologia', 3500),
#     ('Mouse', 'tecnologia', 120),
#     ('Cadeira', 'moveis', 900),
#     ('Mesa', 'moveis', 1200),
#     ('Fone', 'tecnologia', 250)
# ]
#
# Novas regras:
#
# - tecnologia → 15% desconto
# - móveis → 5% desconto
#
# O sistema deve gerar:
#
# - uma nova estrutura contendo:
#     - nome
#     - categoria
#     - preço original
#     - preço final
#
# Exibir:
# - relatório atualizado

produtos = [
    ('Notebook', 'tecnologia', 3500),
    ('Mouse', 'tecnologia', 120),
    ('Cadeira', 'moveis', 900),
    ('Mesa', 'moveis', 1200),
    ('Fone', 'tecnologia', 250)
]
produtos_atualizados = []

desconto = lambda preco, categoria: preco * 0.85 if categoria == 'tecnologia' else preco * 0.95

for produto in produtos:
    nome, categoria, preco = produto
    produtos_atualizados.append((nome, categoria, preco, desconto(preco, categoria)))

print(produtos_atualizados)

# Eu poderia fazer dessa forma - mas não necessariamente é melhor pois começa a ficar muita coisa embolada. Lambda só vale a pena quando: a compactação NÃO prejudica a clareza
produtos_atualizados = []
for produto in produtos:
    nome, categoria, preco = produto
    produtos_atualizados.append((nome, categoria, preco, (lambda preco, categoria: preco * 0.85 if categoria == 'tecnologia' else preco * 0.95)(preco, categoria)))

print(produtos_atualizados)
