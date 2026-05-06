# ==================================================================================================
# 76. Pipeline de benefícios corporativos (RH)
# ==================================================================================================
#
# Após os reajustes, a empresa decidiu automatizar também o processamento de benefícios.
#
# Agora cada funcionário deve passar por:
#
# 1. reajuste salarial
# 2. cálculo de bônus
# 3. classificação de faixa salarial
#
# Dados:
#
# funcionarios = [
#     ('Ana', 'tecnologia', 5000),
#     ('Carlos', 'financeiro', 4000),
#     ('Fernanda', 'tecnologia', 6200),
#     ('Marina', 'rh', 3500)
# ]
#
# Regras:
#
# --------------------------------------------------------------------------------
# Reajuste salarial
# --------------------------------------------------------------------------------
#
# - tecnologia → 12%
# - financeiro → 7%
# - rh → 5%
#
#
# --------------------------------------------------------------------------------
# Bônus anual
# --------------------------------------------------------------------------------
#
# - salários acima de R$6000:
#     bônus de R$1500
#
# - demais funcionários:
#     bônus de R$800
#
#
# --------------------------------------------------------------------------------
# Classificação salarial
# --------------------------------------------------------------------------------
#
# - acima de R$7000:
#     senior
#
# - entre R$4000 e R$7000:
#     pleno
#
# - abaixo de R$4000:
#     junior
#
#
# O sistema deve:
#
# - processar os funcionários em etapas
# - utilizar map para transformar os dados progressivamente
#
#
# O relatório final deve conter:
#
# - nome
# - setor
# - salário original
# - salário reajustado
# - bônus
# - classificação
#
#
# Exibir:
#
# - relatório completo de funcionários
#
funcionarios = [
    ('Ana', 'tecnologia', 5000),
    ('Carlos', 'financeiro', 4000),
    ('Fernanda', 'tecnologia', 6200),
    ('Marina', 'rh', 3500)
]

regras_reajuste = {
    'tecnologia': lambda salario: round(salario * 1.12, 2),
    'financeiro': lambda salario: round(salario * 1.07, 2),
    'rh': lambda salario: round(salario * 1.05, 2)
}

funcionarios_reajuste = list(map(lambda funcionario: (funcionario[0],
                                                         funcionario[1],
                                                         funcionario[2],
                                                         regras_reajuste[funcionario[1]](funcionario[2])
                                                         ),
                                    funcionarios))

print(funcionarios_reajuste)

funcionarios_bonus = list(map(lambda funcionario: (funcionario[0],
                                                        funcionario[1],
                                                        funcionario[2],
                                                        funcionario[3],
                                                        (funcionario[3] + 1500 if funcionario[3] > 6000 else funcionario[3] + 800)
                                                         ),
                                    funcionarios_reajuste))

print(funcionarios_bonus)

funcionarios_classificacao = list(map(lambda funcionario: (funcionario[0],
                                                        funcionario[1],
                                                        funcionario[2],
                                                        funcionario[3],
                                                        funcionario[4],
                                                        'senior' if funcionario[4] > 7000 else 'pleno' if 4000 <= funcionario[4] <= 7000 else 'junior'
                                                         ),
                                    funcionarios_bonus))

print(funcionarios_classificacao)
