# --------------------------------------------------------------------------------------------------
# 6. MINI CHALLENGE — Complete Billing System
# --------------------------------------------------------------------------------------------------
# The store wants a final daily report.
#
# Data:
#
# orders = [
#     [50, 120],
#     [30, 80, 200],
#     [90]
# ]
#
# Rules:
#
# - orders above $200 receive a 15% discount
# - all orders receive a 10% service fee
#
# The system must:
#
# - process each order (discount → service fee)
#
# - generate a report containing:
#     - total number of orders
#     - total billed amount
#     - average order value
#     - highest order value of the day
#
# Rules:
# - the system must be organized into functions
# - each function must have a clear responsibility
#
# Display:
# - complete final report


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

    discounted_value = apply_discount(
        total_value,
        discount_rate
    )

    final_value = apply_service_fee(
        discounted_value,
        service_fee_rate
    )

    return final_value


def process_orders(orders, discount_rate, service_fee_rate):
    processed_values = []

    for order in orders:
        final_value = process_order(
            order,
            discount_rate,
            service_fee_rate
        )

        processed_values.append(final_value)

    return processed_values


def display_report(processed_values):
    total_orders = len(processed_values)

    total_billed = sum(processed_values)

    if total_orders > 0:
        average_order_value = total_billed / total_orders
    else:
        average_order_value = 0

    if processed_values:
        highest_order_value = max(processed_values)
    else:
        highest_order_value = 0

    print(f'Total orders for the day: {total_orders}')
    print(f'Total billed amount: ${total_billed:.2f}')

    if total_orders > 0:
        print(f'Average order value: ${average_order_value:.2f}')
    else:
        print('No orders were processed')

    print(f'Highest order value: ${highest_order_value:.2f}')


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

display_report(processed_values)
