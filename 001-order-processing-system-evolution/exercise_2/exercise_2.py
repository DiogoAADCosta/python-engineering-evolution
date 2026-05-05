# --------------------------------------------------------------------------------------------------
# 2. Service Fee Application
# --------------------------------------------------------------------------------------------------
# The store started charging a service fee on the total order value.
#
# On regular days, the service fee is 10%.
#
# The system now needs to:
# - calculate the total order value
# - apply the service fee to that value
#
# This calculation will be reused in other parts of the system.
#
# Display:
# - original total value
# - total value with service fee



def calculate_total_value(prices):
    return sum(prices)


def apply_service_fee(total_value, fee):
    return total_value * (1 + fee)


prices = [50, 120, 30, 80]
service_fee = 0.1

total_value = calculate_total_value(prices)
total_with_fee = apply_service_fee(total_value, service_fee)

print(f'The total order value is: ${total_value:.2f}')
print(f'The total order value with a 10% service fee is: ${total_with_fee:.2f}')
