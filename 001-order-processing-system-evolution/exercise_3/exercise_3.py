# --------------------------------------------------------------------------------------------------
# 3. Conditional Discounts
# --------------------------------------------------------------------------------------------------
# The store created a discount policy:
#
# - orders above $200 receive a 15% discount
# - smaller orders do not receive a discount
#
# The system must:
# - calculate the total order value
# - check whether the order qualifies for a discount
# - apply the discount when necessary
#
# Then:
# - apply a 10% service fee
#
# Display:
# - original total value
# - final total value


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


prices = [50, 120, 30, 80]

discount_rate = 0.15
service_fee_rate = 0.10

total_value = calculate_total_value(prices)

discounted_value, discount_applied = apply_discount(
    total_value,
    discount_rate
)

final_value = apply_service_fee(discounted_value,service_fee_rate)

print(f'The total order value is: ${total_value:.2f}')

if discount_applied:
    print(f'The total order value with a 15% discount is: ${discounted_value:.2f}')

print(f'The total order value with a 10% service fee is: ${final_value:.2f}')
