# NOI, CoC, Cap Rate Functions
def calculate_noi(gross_rent, vacancy_rate, taxes, insurance, maintenance, mgmt_fee, capex):
    effective_rent = gross_rent * (1 - vacancy_rate)
    total_expenses = taxes + insurance + maintenance + mgmt_fee + capex
    return effective_rent - total_expenses

def calculate_cash_on_cash(annual_noi, annual_debt_service, down_payment):
    return (annual_noi - annual_debt_service) / down_payment

def calculate_cap_rate(annual_noi, purchase_price):
    return annual_noi / purchase_price

