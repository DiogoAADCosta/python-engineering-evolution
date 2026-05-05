# --------------------------------------------------------------------------------------------------
# 1. Simple Order Registration
# --------------------------------------------------------------------------------------------------
# A customer placed an order containing products with the following prices:
#
# [50, 120, 30, 80]
#
# The system needs to calculate the total order value.
#
# This calculation will be reused in other parts of the system,
# so it must be isolated.
#
# Display:
# - total order value

def calculate_total_value(prices):
    return sum(prices)

prices = [50, 120, 30, 80]

total_value = calculate_total_value(prices)

print(f'The total order value is: ${total_value:.2f}')
