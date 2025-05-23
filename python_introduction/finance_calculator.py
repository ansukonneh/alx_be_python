monthly_income = int(input("Enter Your Monthly Income:"))
monthly_expenses = int(input("Enter your total monthly expenses:"))

monthly_saving = monthly_income - monthly_expenses

proected_savings = monthly_saving * 12  + (monthly_saving * 12 * 0.05)

print("Your monthly savings are", monthly_saving)
print("Projected savings after one year, with interest, is:", proected_savings)