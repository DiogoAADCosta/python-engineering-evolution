# ==================================================================================================
# 76. Corporate Benefits Pipeline (HR)
# ==================================================================================================
#
# After the salary adjustments, the company decided to automate
# employee benefits processing as well.
#
# Each employee must now go through:
#
# 1. salary adjustment
# 2. bonus calculation
# 3. salary classification
#
# Data:
#
# employees = [
#     ('Ana', 'technology', 5000),
#     ('Carlos', 'finance', 4000),
#     ('Fernanda', 'technology', 6200),
#     ('Marina', 'hr', 3500)
# ]
#
#
# --------------------------------------------------------------------------------
# Salary adjustment
# --------------------------------------------------------------------------------
#
# - technology → 12%
# - finance → 7%
# - hr → 5%
#
#
# --------------------------------------------------------------------------------
# Annual bonus
# --------------------------------------------------------------------------------
#
# - salaries above $6000:
#     $1500 bonus
#
# - all other employees:
#     $800 bonus
#
#
# --------------------------------------------------------------------------------
# Salary classification
# --------------------------------------------------------------------------------
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
# The system must:
#
# - process employees in stages
# - use map() to progressively transform the data
#
#
# The final report must contain:
#
# - name
# - department
# - original salary
# - adjusted salary
# - bonus
# - classification
#
#
# Display:
#
# - complete employee report


employees = [
    ('Ana', 'technology', 5000),
    ('Carlos', 'finance', 4000),
    ('Fernanda', 'technology', 6200),
    ('Marina', 'hr', 3500)
]

adjustment_rules = {
    'technology': lambda salary: round(salary * 1.12, 2),
    'finance': lambda salary: round(salary * 1.07, 2),
    'hr': lambda salary: round(salary * 1.05, 2)
}

employees_adjustment = list(
    map(
        lambda employee:
        (
            employee[0],
            employee[1],
            employee[2],
            adjustment_rules[employee[1]](employee[2])
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
            (
                employee[3] + 1500
                if employee[3] > 6000
                else employee[3] + 800
            )
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
            (
                'senior'
                if employee[4] > 7000
                else 'mid-level'
                if 4000 <= employee[4] <= 7000
                else 'junior'
            )
        ),
        employees_bonus
    )
)

print(employees_classification)
