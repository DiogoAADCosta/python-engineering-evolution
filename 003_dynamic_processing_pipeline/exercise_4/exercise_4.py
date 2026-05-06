# ==================================================================================================
# 77. MINI DESAFIO — Plataforma configurável de processamento salarial
# ==================================================================================================
#
# A empresa decidiu transformar o sistema em uma plataforma flexível de processamento de RH.
#
# Agora o sistema deve permitir:
#
# - adicionar novas etapas de processamento
# - trocar regras sem alterar o fluxo principal
# - reutilizar o mesmo pipeline para diferentes políticas internas
#
#
# Dados:
#
# funcionarios = [
#     ('Ana', 'tecnologia', 5000),
#     ('Carlos', 'financeiro', 4000),
#     ('Fernanda', 'tecnologia', 6200),
#     ('Marina', 'rh', 3500),
#     ('Rafael', 'financeiro', 8000)
# ]
#
#
# O sistema possuirá:
#
# - etapas de reajuste
# - etapas de bônus
# - etapas de classificação
# - etapas de auditoria salarial
#
#
# Novas regras:
#
# - funcionários acima de R$9000 após processamento:
#     devem receber status:
#         'auditoria'
#
# - os demais:
#     recebem status:
#         'normal'
#
#
# Regras importantes:
#
# - o pipeline principal NÃO pode conter regras fixas de negócio
#
# - as transformações devem ser configuráveis
#
# - o sistema deve permitir adicionar novas etapas
#   sem reescrever o fluxo principal
#
# - o processamento deve continuar utilizando map
#
#
# O relatório final deve conter:
#
# - nome
# - setor
# - salário original
# - salário final
# - bônus
# - classificação
# - status operacional
#
#
# Exibir:
#
# - relatório corporativo completo


funcionarios = [
    ('Ana', 'tecnologia', 5000),
    ('Carlos', 'financeiro', 4000),
    ('Fernanda', 'tecnologia', 6200),
    ('Marina', 'rh', 3500),
    ('Rafael', 'financeiro', 8000)
]

regras_reajuste = {
    'tecnologia': lambda salario: round(salario * 1.12, 2),
    'financeiro': lambda salario: round(salario * 1.07, 2),
    'rh': lambda salario: round(salario * 1.05, 2)
}

etapas = {
    'reajuste': lambda setor, salario: regras_reajuste[setor](salario),
    'bonus': lambda salario: salario + 1500 if salario > 6000 else salario + 800,
    'classificacao': lambda salario: 'senior' if salario > 7000 else 'pleno' if 4000 <= salario <= 7000 else 'junior',
    'auditoria': lambda salario: 'auditoria' if salario > 9000 else 'normal'
}

funcionarios_reajuste = list(map(lambda funcionario: (funcionario[0],
                                                         funcionario[1],
                                                         funcionario[2],
                                                         etapas['reajuste'](funcionario[1], funcionario[2])
                                                         ),
                                    funcionarios))

print(funcionarios_reajuste)

funcionarios_bonus = list(map(lambda funcionario: (funcionario[0],
                                                        funcionario[1],
                                                        funcionario[2],
                                                        funcionario[3],
                                                        etapas['bonus'](funcionario[3])
                                                         ),
                                    funcionarios_reajuste))

print(funcionarios_bonus)

funcionarios_classificacao = list(map(lambda funcionario: (funcionario[0],
                                                        funcionario[1],
                                                        funcionario[2],
                                                        funcionario[3],
                                                        funcionario[4],
                                                        etapas['classificacao'](funcionario[4])
                                                         ),
                                    funcionarios_bonus))

print(funcionarios_classificacao)

funcionarios_auditoria = list(map(lambda funcionario: (funcionario[0],
                                                        funcionario[1],
                                                        funcionario[2],
                                                        funcionario[3],
                                                        funcionario[4],
                                                        funcionario[5],
                                                        etapas['auditoria'](funcionario[4])
                                                         ),
                                    funcionarios_classificacao))

print(funcionarios_auditoria)
