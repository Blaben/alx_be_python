monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))


#converting the str values to integer values
#float(monthly_income)
#float(monthly_expense)

monthly_savings = monthly_income - monthly_expenses
annual_savings = monthly_savings * 12
interest = annual_savings * 0.05
projected_savings = annual_savings + interest

print(f"\nYour monthly savings are {round(monthly_savings)}")
print(f"Projected savings after one year, with interest, is: {round(projected_savings)}")
