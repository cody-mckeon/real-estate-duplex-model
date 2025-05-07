def generate_text_report(
    address,
    cap_rate,
    coc_return,
    irr,
    annual_rent,
    estimated_resale,
    purchase_price,
    down_payment,
    loan_rate,
    loan_term_years,
    property_tax,
    insurance,
    vacancy_rate,
    mgmt_pct,
    maintenance_pct,
    capex_cost,
    closing_costs
):
    report = f"""🏠 Investment Summary: {address}

Key Metrics:
• Cap Rate: {cap_rate:.2%} – Return on property without financing (NOI ÷ Purchase Price)
• Cash-on-Cash Return: {coc_return:.2%} – Annual return on cash invested after expenses
• 5-Year IRR: {irr:.2%} – Annualized return with appreciation and resale
• Annual Rent: ${annual_rent:,.2f}
• Estimated Resale Price (Year 5): ${estimated_resale:,.2f}

Assumptions:
• Purchase Price: ${purchase_price:,.2f}
• Down Payment: ${down_payment:,.2f} ({(down_payment / purchase_price):.0%})
• Loan: {loan_term_years} years @ {loan_rate:.2%}
• Property Taxes: ${property_tax:,.2f}/year
• Insurance: ${insurance:,.2f}/year
• Vacancy Rate: {vacancy_rate:.0%}
• Management Fee: {mgmt_pct:.0%} of rent
• Maintenance & CapEx: {maintenance_pct:.0%} of rent
• Make-Ready CapEx: ${capex_cost:,.2f}
• Closing Costs: ${closing_costs:,.2f} ({(closing_costs / purchase_price):.0%})

Summary:
This Lansing duplex offers solid cash flow and long-term upside in a landlord-friendly market. Great fit for a conservative rental portfolio.

📩 Let me know if you'd like the full model or to walk through the numbers.
"""
    return report


def save_report_to_txt(filename, report):
    with open(filename, "w") as f:
        f.write(report)
    print(f"✅ Report saved as {filename}")
# Formatting and print / output logic
