# ==================================================================================================
# 3. Product Processing with Context (E-commerce)
# ==================================================================================================
#
# The store system no longer works only with prices.
#
# Now each product contains:
#
# - name
# - category
# - price
#
# Data:
#
# products = [
#     ('Notebook', 'technology', 3500),
#     ('Mouse', 'technology', 120),
#     ('Chair', 'furniture', 900),
#     ('Desk', 'furniture', 1200),
#     ('Headphones', 'technology', 250)
# ]
#
# New rules:
#
# - technology → 15% discount
# - furniture → 5% discount
#
# The system must generate:
#
# - a new structure containing:
#     - name
#     - category
#     - original price
#     - final price
#
# Display:
# - updated report

products = [
    ('Notebook', 'technology', 3500),
    ('Mouse', 'technology', 120),
    ('Chair', 'furniture', 900),
    ('Desk', 'furniture', 1200),
    ('Headphones', 'technology', 250)
]

updated_products = []

discount = lambda price, category: price * 0.85 if category == 'technology' else price * 0.95

for product in products:
    name, category, price = product
    updated_products.append((name, category, price, discount(price, category)))

print(updated_products)

# I could also do it this way — but it is not necessarily better,
# because the code starts becoming too cluttered.
#
# Lambda is only worth it when:
# compactness DOES NOT hurt clarity.

updated_products = []

for product in products:
    name, category, price = product

    updated_products.append(
        (
            name,
            category,
            price,
            (
                lambda price, category:
                price * 0.85 if category == 'technology'
                else price * 0.95
            )(price, category)
        )
    )

print(updated_products)
