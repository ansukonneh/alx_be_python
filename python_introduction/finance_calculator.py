monthly_income = float(input("Enter Your Monthly Income:"))
monthly_expenses = float(input("Enter your total monthly expenses:"))

monthly_saving = monthly_income - monthly_expenses

projected_savings = monthly_saving * 12  + (monthly_saving * 12 * (0.05))

print(f"Your monthly savings are ${monthly_saving:.2f}")
print(f"Projected savings after one year, with interest, is: ${projected_savings:.2f}")