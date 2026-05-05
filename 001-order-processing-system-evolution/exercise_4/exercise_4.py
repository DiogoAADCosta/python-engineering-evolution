# --------------------------------------------------------------------------------------------------
# 4. Multiple Order Processing
# --------------------------------------------------------------------------------------------------
# The store now receives multiple orders throughout the day.
#
# Each order contains a list of product prices:
#
# orders = [
#     [50, 120],
#     [30, 80, 200],
#     [90]
# ]
#
# The system must:
# - calculate the total value of each order
# - generate a summary containing all order totals
#
# Rules:
# - each order must be processed independently
#
# Display:
# - list of order totals
# - total revenue for the day


def calculate_total_value(prices):
    return sum(prices)


def apply_discount(total_value, discount_rate):
    if total_value > 200:
        discount_applied = True
        return total_value * (1 - discount_rate), discount_applied
    else:
        discount_applied = False
        return total_value, discount_applied


def apply_service_fee(total_value, service_fee_rate):
    return total_value * (1 + service_fee_rate)


def calculate_orders(orders):
    order_totals = []

    for order in orders:
        total_value = calculate_total_value(order)
        order_totals.append(total_value)

    return order_totals


orders = [
    [50, 120],
    [30, 80, 200],
    [90]
]

discount_rate = 0.15
service_fee_rate = 0.10

order_totals = calculate_orders(orders)

print('Order total values:')

for final_value in order_totals:
    print(f'${final_value:.2f}')

print(f'\nTotal revenue for the day:\n${sum(order_totals):.2f}')
