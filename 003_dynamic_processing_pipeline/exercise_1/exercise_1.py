# ==================================================================================================
# 1. Atualização automática de salários (RH)
# ==================================================================================================
#
# O setor de RH iniciou um reajuste salarial anual.
#
# O sistema possui uma lista contendo os salários atuais:
#
# salarios = [2500, 3200, 1800, 5000, 4100]
#
# A empresa definiu:
#
# - reajuste de 8% para todos os funcionários
#
# O sistema deve gerar:
#
# - uma nova lista contendo os salários atualizados
#
# Exibir:
#
# - salários originais
# - salários reajustados

salarios = [2500, 3200, 1800, 5000, 4100]

salarios_atualizados = list(map(lambda salario: round(salario * 1.08), salarios))

print(salarios)
print(salarios_atualizados)
