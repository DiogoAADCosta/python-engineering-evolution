# --------------------------------------------------------------------------------------------------
# 5. Separation of Responsibilities
# --------------------------------------------------------------------------------------------------
# The system started becoming difficult to maintain.
#
# You now need to reorganize the code so that each part
# has a clear responsibility:
#
# - total calculation
# - discount application
# - service fee application
#
# The system must:
# - use these functions to process each order
#
# Display:
# - final processed value for each order


def calculate_total_value(prices):
    return sum(prices)


def apply_discount(total_value, discount_rate):
    if total_value > 200:
        return total_value * (1 - discount_rate)
    else:
        return total_value


def apply_service_fee(total_value, service_fee_rate):
    return total_value * (1 + service_fee_rate)


def process_order(prices, discount_rate, service_fee_rate):
    total_value = calculate_total_value(prices)

    discounted_value = apply_discount(total_value, discount_rate)

    final_value = apply_service_fee(discounted_value, service_fee_rate)

    return final_value


def process_orders(orders, discount_rate, service_fee_rate):
    processed_values = []

    for order in orders:
        final_value = process_order(order, discount_rate, service_fee_rate )
        processed_values.append(final_value)
    return processed_values


orders = [
    [50, 120],
    [30, 80, 200],
    [90]
]

discount_rate = 0.15
service_fee_rate = 0.10

processed_values = process_orders(
    orders,
    discount_rate,
    service_fee_rate
)

print('Final processed values for each order:')

for final_value in processed_values:
    print(f'${final_value:.2f}')
