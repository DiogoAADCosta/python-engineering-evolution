# ==================================================================================================
# 1. Simple Price Update (E-commerce)
# ==================================================================================================
#
# An e-commerce company started a promotional campaign.
#
# The system contains a list of product prices:
#
# prices = [120, 80, 250, 40, 310]
#
# The commercial team decided to apply:
#
# - a 10% discount to all products
#
# The system must generate:
#
# - a new list containing the updated prices
#
# Display:
# - original prices
# - promotional prices

prices = [120, 80, 250, 40, 310]
updated_prices = []

updated_price = lambda x: x * 0.9

for price in prices:
    updated_prices.append(updated_price(price))

print(prices)
print(updated_prices)
