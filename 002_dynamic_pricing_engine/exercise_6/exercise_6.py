# ==================================================================================================
# 6. Campaign Priority System (E-commerce)
# ==================================================================================================
#
# The commercial department realized that some campaigns
# CANNOT be combined together.
#
# The system must now decide:
#
# - which campaigns can coexist
# - which campaigns have priority
#
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
#
# Active campaigns:
#
# active_campaigns = [
#     'black_friday',
#     'christmas',
#     'loyalty'
# ]
#
#
# --------------------------------------------------------------------------------
# Promotional rules
# --------------------------------------------------------------------------------
#
# black_friday:
#
# - technology → 30% discount
# - furniture → 15% discount
#
#
# christmas:
#
# - technology → 20% discount
# - furniture → 10% discount
#
#
# loyalty:
#
# - products below $500:
#     receive an additional 5% discount
#
# - products equal to or above $500:
#     receive an additional 10% discount
#
#
# --------------------------------------------------------------------------------
# Priority rules
# --------------------------------------------------------------------------------
#
# - black_friday and christmas CANNOT be applied together
#
# - when both are active:
#     black_friday has priority
#
# - loyalty can still be combined
#   with any seasonal campaign
#
#
# The system must:
#
# - dynamically decide which campaigns will be applied
# - ignore campaigns blocked by priority rules
# - apply discounts sequentially
#
#
# The system must generate:
#
# - name
# - category
# - original price
# - final price
# - effectively applied campaigns
# - ignored campaigns
#
#
# Important rules:
#
# - decisions must happen dynamically
#
# - the main loop CANNOT contain:
#     - if campaign == ...
#     - elif campaign == ...
#
# - campaigns must continue being configured
#   using lambdas
#
#
# Display:
#
# - complete processing report


products = [
    ('Notebook', 'technology', 3500),
    ('Mouse', 'technology', 120),
    ('Chair', 'furniture', 900),
    ('Desk', 'furniture', 1200)
]

updated_products = []

ignored_campaigns = []

active_campaigns = [
    'black_friday',
    'christmas',
    'loyalty'
]

price_rules = {
    'black_friday':
        (
            lambda price, category:
            price * 0.7 if category == 'technology'
            else price * 0.85
        ),

    'christmas':
        (
            lambda price, category:
            price * 0.8 if category == 'technology'
            else price * 0.9
        ),

    'loyalty':
        (
            lambda price, category:
            price * 0.95 if price < 500
            else price * 0.9
        )
}


if 'black_friday' in active_campaigns and 'christmas' in active_campaigns:
    active_campaigns.remove('christmas')
    ignored_campaigns.append('christmas')


for product in products:
    name, category, original_price = product
    price = original_price
    for campaign in active_campaigns:
        price = price_rules[campaign](price, category)
    updated_products.append(
        (
            name,
            category,
            original_price,
            price
        )
    )

print(f'Updated products: {updated_products}')
print(f'Applied campaigns: {active_campaigns}')
print(f'Ignored campaigns: {ignored_campaigns}')
