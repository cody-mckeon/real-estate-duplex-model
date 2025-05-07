# NOI, CoC, Cap Rate Functions
def calculate_noi(gross_rent, vacancy_rate, taxes, insurance, maintenance, mgmt_fee, capex_reserve):
    effective_rent = gross_rent * (1 - vacancy_rate)
    total_expenses = taxes + insurance + maintenance + mgmt_fee + capex_reserve
    return effective_rent - total_expenses

def calculate_cash_on_cash(annual_noi, annual_debt_service, down_payment, make_ready_cost, closing_costs):
    total_investment = down_payment + make_ready_cost + closing_costs
    return (annual_noi - annual_debt_service) / total_investment

def calculate_cap_rate(annual_noi, purchase_price):
    return annual_noi / purchase_price

