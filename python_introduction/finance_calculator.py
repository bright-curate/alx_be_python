# Ask the user for their monthly money amounts (use float so cents work)
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses

# Project annual savings with 5% interest
annual_savings_before_interest = monthly_savings * 12
projected_savings = annual_savings_before_interest * (1 + 0.05)  # same as * 1.05

# Print the results (formatted to two decimal places)
print(f"Your monthly savings are: {monthly_savings:.2f}")
print(f"Projected savings after 1 year with 5% interest: {projected_savings:.2f}")