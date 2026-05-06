# ==================================================================================================
# 2. Processamento de funcionários por setor (RH)
# ==================================================================================================
#
# Após o reajuste geral,
# a empresa percebeu que cada setor
# precisa de uma política salarial diferente.
#
# Agora cada funcionário possui:
#
# - nome
# - setor
# - salário
#
# Dados:
#
# funcionarios = [
#     ('Ana', 'tecnologia', 5000),
#     ('Carlos', 'financeiro', 4000),
#     ('Fernanda', 'tecnologia', 6200),
#     ('Marina', 'rh', 3500),
#     ('João', 'financeiro', 4500)
# ]
#
# Novas regras:
#
# - tecnologia → 12% reajuste
# - financeiro → 7% reajuste
# - rh → 5% reajuste
#
# O sistema deve gerar:
#
# - uma nova estrutura contendo:
#     - nome
#     - setor
#     - salário original
#     - salário reajustado
#
# Regras importantes:
#
# - o processamento deve ocorrer usando map
#
# Exibir:
#
# - relatório atualizado de salários
#
funcionarios = [
    ('Ana', 'tecnologia', 5000),
    ('Carlos', 'financeiro', 4000),
    ('Fernanda', 'tecnologia', 6200),
    ('Marina', 'rh', 3500),
    ('João', 'financeiro', 4500)
]

regras = {
    'tecnologia': lambda salario: round(salario * 1.12, 2),
    'financeiro': lambda salario: round(salario * 1.07, 2),
    'rh': lambda salario: round(salario * 1.05, 2)
}

salarios_atualizados = list(map(lambda funcionario: (funcionario[0], funcionario[1], funcionario[2], regras[funcionario[1]](funcionario[2])), funcionarios))

print(salarios_atualizados)
