#Ask user to enter need variables
monthly_income = int(input("Enter your monthly income:"))
monthly_expenses = int(input("Enter your total monthly expenses:"))

#Calculation for monthly savings
monthly_savings = monthly_income - monthly_expenses

#Calculation for annual compound savings interests
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

print("Your monthly savings are:$", monthly_savings)
print("Projected savings after one year, with interest, is:$", projected_savings)