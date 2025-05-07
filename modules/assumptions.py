# assumptions.py - stores default property values

# One-time costs
MAKE_READY_COST = 2000
CLOSING_COSTS = 8094  # Estimate or percent of purchase

# Property and financing
PROPERTY_PRICE = 134900
DOWN_PAYMENT_PCT = 0.20
LOAN_RATE = 0.07
LOAN_TERM_YEARS = 30

# Income & expenses
RENT_MONTHLY = 1700
VACANCY_RATE = 0.05
TAXES = 4638.11
INSURANCE = 1670
MAINTENANCE = RENT_MONTHLY * 0.05 * 12
MGMT_FEE = RENT_MONTHLY * 0.08 * 12

# CapEx reserve (spread over time)
ROOF = 10000 / 20
HVAC = 5000 / 15
WATER_HEATER = 1000 / 10
CAPEX_RESERVE = ROOF + HVAC + WATER_HEATER

# Resale assumptions
APPRECIATION_RATE = 0.03
HOLD_YEARS = 5
SELLING_COST_PCT = 0.06

