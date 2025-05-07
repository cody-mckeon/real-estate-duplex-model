# Mortgage-related functions

def mortgage_payment(principal, annual_rate, years):
    r = annual_rate / 12
    n = years * 12
    if r == 0:
        return principal / n
    return principal * (r * (1 + r)**n) / ((1 + r)**n - 1)

