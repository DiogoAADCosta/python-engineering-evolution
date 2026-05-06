# ==================================================================================================
# 1. Automatic Salary Adjustment (HR)
# ==================================================================================================
#
# The HR department started the annual salary adjustment process.
#
# The system contains a list of current salaries:
#
# salaries = [2500, 3200, 1800, 5000, 4100]
#
# The company defined:
#
# - an 8% salary increase for all employees
#
# The system must generate:
#
# - a new list containing the updated salaries
#
# Display:
#
# - original salaries
# - adjusted salaries


salaries = [2500, 3200, 1800, 5000, 4100]

updated_salaries = list(
    map(lambda salary: round(salary * 1.08), salaries))

print(salaries)
print(updated_salaries)
