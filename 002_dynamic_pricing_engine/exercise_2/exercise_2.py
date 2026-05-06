# ==================================================================================================
# 2. Promotional Campaign by Price Range
# ==================================================================================================
#
# After the first campaign,
# the company realized that cheaper products
# need larger discounts to improve conversion.
#
# Data:
#
# prices = [120, 80, 250, 40, 310]
#
# New rules:
#
# - products below R$100 receive a 20% discount
# - products equal to or above R$100 receive a 10% discount
#
# The system must generate:
#
# - a new list containing the final prices
#
# Display:
# - updated prices
#

prices = [120, 80, 250, 40, 310]

discount = lambda x: x * 0.8 if x < 100 else x * 0.9
updated_prices = [discount(price) for price in prices]

print(updated_prices)
