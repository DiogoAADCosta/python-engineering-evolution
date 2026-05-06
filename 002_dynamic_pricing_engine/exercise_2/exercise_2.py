# ==================================================================================================
# 2. Campanha promocional por faixa de preço
# ==================================================================================================
#
# Após a primeira campanha,
# a empresa percebeu que produtos mais baratos
# precisam de descontos maiores para gerar conversão.
#
# Dados:
#
# precos = [120, 80, 250, 40, 310]
#
# Novas regras:
#
# - produtos abaixo de R$100 recebem 20% de desconto
# - produtos acima ou iguais a R$100 recebem 10%
#
# O sistema deve gerar:
#
# - uma nova lista contendo os preços finais
#
# Exibir:
# - preços atualizados
#
precos = [120, 80, 250, 40, 310]

desconto = lambda x: x * 0.8 if x < 100 else x * 0.9
precos_atualizados = [desconto(preco) for preco in precos]

print(precos_atualizados)
