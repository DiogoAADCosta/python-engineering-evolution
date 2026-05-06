# ==================================================================================================
# 2. Employee Processing by Department (HR)
# ==================================================================================================
#
# After the general salary adjustment,
# the company realized that each department
# requires a different salary policy.
#
# Each employee now contains:
#
# - name
# - department
# - salary
#
# Data:
#
# employees = [
#     ('Ana', 'technology', 5000),
#     ('Carlos', 'finance', 4000),
#     ('Fernanda', 'technology', 6200),
#     ('Marina', 'hr', 3500),
#     ('João', 'finance', 4500)
# ]
#
# New rules:
#
# - technology → 12% adjustment
# - finance → 7% adjustment
# - hr → 5% adjustment
#
# The system must generate:
#
# - a new structure containing:
#     - name
#     - department
#     - original salary
#     - adjusted salary
#
# Important rules:
#
# - processing must occur using map()
#
# Display:
#
# - updated salary report


employees = [
    ('Ana', 'technology', 5000),
    ('Carlos', 'finance', 4000),
    ('Fernanda', 'technology', 6200),
    ('Marina', 'hr', 3500),
    ('João', 'finance', 4500)
]

rules = {
    'technology': lambda salary: round(salary * 1.12, 2),
    'finance': lambda salary: round(salary * 1.07, 2),
    'hr': lambda salary: round(salary * 1.05, 2)
}

updated_salaries = list(
    map(
        lambda employee:
        (
            employee[0],
            employee[1],
            employee[2],
            rules[employee[1]](employee[2])
        ),
        employees
    )
)

print(updated_salaries)
