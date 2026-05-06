# ==================================================================================================
# 72. Simultaneous Campaign System (E-commerce)
# ==================================================================================================
#
# The company started running multiple promotional campaigns
# at the same time.
#
# A product can now receive:
#
# - the main seasonal campaign discount
# - an additional loyalty bonus discount
#
# depending on the active campaigns in the system.
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
# Active campaigns:
#
# active_campaigns = [
#     'black_friday',
#     'loyalty'
# ]
#
#
# --------------------------------------------------------------------------------
# Seasonal campaigns
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
# --------------------------------------------------------------------------------
# Complementary campaign
# --------------------------------------------------------------------------------
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
# Important rules:
#
# - seasonal and loyalty campaigns can be applied together
# - discounts must be applied sequentially
# - the system must support multiple active campaigns
# - rules must be configured using lambdas
#
#
# The system must:
#
# - identify active campaigns
# - automatically apply corresponding rules
# - accumulate discounts correctly
#
#
# The system must generate:
#
# - name
# - category
# - original price
# - final price
# - applied campaigns
#
#
# Display:
# - complete updated product report


products = [
    ('Notebook', 'technology', 3500),
    ('Mouse', 'technology', 120),
    ('Chair', 'furniture', 900),
    ('Desk', 'furniture', 1200)
]

updated_products = []

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
    ),

    (
        lambda campaign: campaign == 'loyalty',
        lambda price, category:
        price * 0.95 if price < 500
        else price * 0.9
    )
]

# If a new campaign is created, just need to add its rules in the list "rules" and its name here in active_campaign.
# Might as well simply remove old campaigns from active_campaigns if they are not active
active_campaigns = [  
    'black_friday',
    'christmas',
    'loyalty'
]

for product in products:
    name, category, original_price = product
    price = original_price
    for campaign in active_campaigns:
        for rule, action in rules:
            if rule(campaign):
                price = action(price, category)
    updated_products.append(
        (
            name,
            category,
            original_price,
            price
        )
    )

for product in updated_products:
    print(product)
