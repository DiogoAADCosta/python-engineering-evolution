# ==================================================================================================
# 5. Structural Evolution — Dynamic Corporate Processing Pipeline
# ==================================================================================================
#
# After the growth of the HR system,
# the company realized that the current model
# started generating maintenance problems.
#
# The current pipeline contains:
#
# - multiple processing stages
# - independent rules
# - progressive data transformation
#
# However, the system started presenting:
#
# - excessive positional indexing
# - difficulty adding new fields
# - difficulty adding new stages
# - the need to modify the main flow
#   whenever the pipeline grows
#
#
# The technical team decided to perform
# a complete structural refactor.
#
#
# --------------------------------------------------------------------------------
# NEW SYSTEM GOAL
# --------------------------------------------------------------------------------
#
# The pipeline must become:
#
# - fully configurable
# - reusable
# - extensible
# - decoupled from specific business rules
#
#
# The system must:
#
# - abandon tuple-based positional structures
#
# - use named structures
#   to represent employees
#
# - allow adding new stages
#   without changing the main flow
#
# - process all stages dynamically
#
#
# --------------------------------------------------------------------------------
# DATA
# --------------------------------------------------------------------------------
#
# employees = [
#     {
#         'name': 'Ana',
#         'department': 'technology',
#         'original_salary': 5000
#     },
#
#     {
#         'name': 'Carlos',
#         'department': 'finance',
#         'original_salary': 4000
#     },
#
#     {
#         'name': 'Fernanda',
#         'department': 'technology',
#         'original_salary': 6200
#     },
#
#     {
#         'name': 'Marina',
#         'department': 'hr',
#         'original_salary': 3500
#     },
#
#     {
#         'name': 'Rafael',
#         'department': 'finance',
#         'original_salary': 8000
#     }
# ]
#
#
# --------------------------------------------------------------------------------
# PIPELINE STAGES
# --------------------------------------------------------------------------------
#
# The system will continue containing:
#
# - salary adjustment
# - bonus calculation
# - salary classification
# - operational audit
#
#
# --------------------------------------------------------------------------------
# RULES
# --------------------------------------------------------------------------------
#
# Adjustment:
#
# - technology → 12%
# - finance → 7%
# - hr → 5%
#
#
# Bonus:
#
# - salaries above $6000:
#     $1500 bonus
#
# - others:
#     $800 bonus
#
#
# Classification:
#
# - above $7000:
#     senior
#
# - between $4000 and $7000:
#     mid-level
#
# - below $4000:
#     junior
#
#
# Audit:
#
# - final salaries above $9000:
#     status → audit
#
# - others:
#     status → normal
#
#
# --------------------------------------------------------------------------------
# IMPORTANT RULES
# --------------------------------------------------------------------------------
#
# - the main flow CANNOT know:
#
#     - stage names
#     - specific rules
#     - number of stages
#
#
# - the system must support:
#
#     - adding stages
#     - removing stages
#     - replacing stages
#
#   without changing the main pipeline
#
#
# - stages must execute dynamically
#
#
# - processing must continue using map()
#
#
# --------------------------------------------------------------------------------
# FINAL GOAL
# --------------------------------------------------------------------------------
#
# The system must generate a report containing:
#
# - name
# - department
# - original salary
# - adjusted salary
# - bonus
# - classification
# - operational status
#
#
# Display:
#
# - final corporate report


employees = [
    {
        'name': 'Ana',
        'department': 'technology',
        'original_salary': 5000
    },

    {
        'name': 'Carlos',
        'department': 'finance',
        'original_salary': 4000
    },

    {
        'name': 'Fernanda',
        'department': 'technology',
        'original_salary': 6200
    },

    {
        'name': 'Marina',
        'department': 'hr',
        'original_salary': 3500
    },

    {
        'name': 'Rafael',
        'department': 'finance',
        'original_salary': 8000
    }
]

adjustment_rules = {
    'technology': lambda salary: round(salary * 1.12, 2),
    'finance': lambda salary: round(salary * 1.07, 2),
    'hr': lambda salary: round(salary * 1.05, 2)
}

stages = {
    'adjustment': lambda department, salary: adjustment_rules[department](salary),
    'bonus': lambda department, salary: salary + 1500 if salary > 6000 else salary + 800,
    'classification': lambda department, salary: 'senior' if salary > 7000 else 'mid-level' if 4000 <= salary <= 7000 else 'junior',
    'audit': lambda department, salary: 'audit' if salary > 9000 else 'normal'
}


def process_stage(employee, stage, salary):
    salary = stages[stage](
        employee['department'],
        employee[salary]
    )
    employee[stage] = salary
    return employee


for stage in stages:
    updated_employees = list(map(process_stage, employees))
    for index, employee in enumerate(employees):
        employee[stage] = updated_employees[index]


for employee in employees:
    print(employee)
