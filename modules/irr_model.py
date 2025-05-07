import numpy_financial as npf

def calculate_resale_price(purchase_price, appreciation_rate=0.03, years=5):
    return purchase_price * (1 + appreciation_rate) ** years

def calculate_remaining_loan_balance(loan_amount, annual_rate, loan_term_years, years_elapsed):
    r = annual_rate / 12
    n = loan_term_years * 12
    p = years_elapsed * 12
    if annual_rate == 0:
        return loan_amount * (1 - p / n)
    monthly_payment = loan_amount * (r * (1 + r) ** n) / ((1 + r) ** n - 1)
    return loan_amount * ((1 + r)**n - (1 + r)**p) / ((1 + r)**n - 1)

def calculate_irr(annual_cash_flow, initial_investment, resale_price, loan_balance, selling_cost_pct=0.06):
    net_proceeds = resale_price * (1 - selling_cost_pct) - loan_balance
    cash_flows = [-initial_investment] + [annual_cash_flow] * 4 + [annual_cash_flow + net_proceeds]
    return npf.irr(cash_flows)
