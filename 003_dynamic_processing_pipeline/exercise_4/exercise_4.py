# ==================================================================================================
# 77. Configurable Salary Processing Platform (HR)
# ==================================================================================================
#
# The company decided to transform the HR system
# into a flexible employee-processing platform.
#
# The system must now support:
#
# - adding new processing stages
# - changing rules without modifying the main flow
# - reusing the same pipeline for different internal policies
#
#
# Data:
#
# employees = [
#     ('Ana', 'technology', 5000),
#     ('Carlos', 'finance', 4000),
#     ('Fernanda', 'technology', 6200),
#     ('Marina', 'hr', 3500),
#     ('Rafael', 'finance', 8000)
# ]
#
#
# The system will contain:
#
# - salary adjustment stages
# - bonus stages
# - classification stages
# - salary audit stages
#
#
# New rules:
#
# - employees above $9000 after processing:
#     must receive status:
#         'audit'
#
# - all others:
#     receive status:
#         'normal'
#
#
# Important rules:
#
# - the main pipeline CANNOT contain fixed business rules
#
# - transformations must be configurable
#
# - the system must support adding new stages
#   without rewriting the main flow
#
# - processing must continue using map()
#
#
# The final report must contain:
#
# - name
# - department
# - original salary
# - final salary
# - bonus
# - classification
# - operational status
#
#
# Display:
#
# - complete corporate employee report


employees = [
    ('Ana', 'technology', 5000),
    ('Carlos', 'finance', 4000),
    ('Fernanda', 'technology', 6200),
    ('Marina', 'hr', 3500),
    ('Rafael', 'finance', 8000)
]

adjustment_rules = {
    'technology': lambda salary: round(salary * 1.12, 2),
    'finance': lambda salary: round(salary * 1.07, 2),
    'hr': lambda salary: round(salary * 1.05, 2)
}

stages = {
    'adjustment': lambda department, salary: adjustment_rules[department](salary),
    'bonus': lambda salary: salary + 1500 if salary > 6000 else salary + 800,
    'classification': lambda salary: 'senior' if salary > 7000 else 'mid-level' if 4000 <= salary <= 7000 else 'junior',
    'audit': lambda salary: 'audit' if salary > 9000 else 'normal'
}

employees_adjustment = list(
    map(
        lambda employee:
        (
            employee[0],
            employee[1],
            employee[2],
            stages['adjustment'](employee[1], employee[2])
        ),
        employees
    )
)

print(employees_adjustment)


employees_bonus = list(
    map(
        lambda employee:
        (
            employee[0],
            employee[1],
            employee[2],
            employee[3],
            stages['bonus'](employee[3])
        ),
        employees_adjustment
    )
)

print(employees_bonus)


employees_classification = list(
    map(
        lambda employee:
        (
            employee[0],
            employee[1],
            employee[2],
            employee[3],
            employee[4],
            stages['classification'](employee[4])
        ),
        employees_bonus
    )
)

print(employees_classification)


employees_audit = list(
    map(
        lambda employee:
        (
            employee[0],
            employee[1],
            employee[2],
            employee[3],
            employee[4],
            employee[5],
            stages['audit'](employee[4])
        ),
        employees_classification
    )
)

print(employees_audit)
