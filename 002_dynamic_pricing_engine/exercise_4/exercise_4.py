# ==================================================================================================
# 4. Seasonal Campaign System
# ==================================================================================================
#
# The company now works with different campaigns
# depending on the season of the year.
#
# Each campaign has its own discount rules.
#
# Data:
#
# products = [
#     ('Notebook', 'technology', 3500),
#     ('Mouse', 'technology', 120),
#     ('Chair', 'furniture', 900),
#     ('Desk', 'furniture', 1200)
# ]
#
# campaign = 'black_friday'
#
# Rules:
#
# - black_friday:
#     technology → 30%
#     furniture → 15%
#
# - christmas:
#     technology → 20%
#     furniture → 10%
#
# The system must automatically apply:
#
# - the correct rule for the current campaign
#
# Display:
# - updated products
# - applied campaign


# Solution 1

products = [
    ('Notebook', 'technology', 3500),
    ('Mouse', 'technology', 120),
    ('Chair', 'furniture', 900),
    ('Desk', 'furniture', 1200)
]

updated_products = []

campaign = 'christmas'

for product in products:
    name, category, price = product

    if campaign == 'black_friday':
        updated_products.append(
            (
                name,
                category,
                price,
                (
                    lambda price, category:
                    price * 0.7 if category == 'technology'
                    else price * 0.85
                )(price, category)
            )
        )

    elif campaign == 'christmas':
        updated_products.append(
            (
                name,
                category,
                price,
                (
                    lambda price, category:
                    price * 0.8 if category == 'technology'
                    else price * 0.9
                )(price, category)
            )
        )

for product in updated_products:
    print(product)


# Solution 2 (Separating rules using lambdas)

products = [
    ('Notebook', 'technology', 3500),
    ('Mouse', 'technology', 120),
    ('Chair', 'furniture', 900),
    ('Desk', 'furniture', 1200)
]

rules = [
    (
        lambda campaign: campaign == 'black_friday',
        lambda price, category:
        price * 0.7 if category == 'technology'
        else price * 0.85
    ),

    (
        lambda campaign: campaign == 'christmas',
        lambda price, category:
        price * 0.8 if category == 'technology'
        else price * 0.9
    )
]

updated_products = []

campaign = 'christmas'

for product in products:
    name, category, price = product

    for condition, action in rules:

        if condition(campaign):
            updated_products.append(
                (
                    name,
                    category,
                    price,
                    action(price, category)
                )
            )

for product in updated_products:
    print(product)
