"""MIT6_0001F16_ps1.pdf

#Part A: House Hunting (NOW PART B UPDATED)"""

annual_salary = int(input("Enter your annual salary:   "))
portion_saved = float(input("Enter portion of salary to \
be saved, as decimal:   "))
total_cost = int(input("Enter cost of your dream home:   "))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal:    "))

portion_down_payment = 0.25 * total_cost
current_savings = 0

number_of_months = 0
while current_savings < portion_down_payment:
    if number_of_months % 6 == 0 and number_of_months != 0:
        annual_salary += semi_annual_raise * annual_salary
        current_savings += portion_saved * annual_salary / 12 + current_savings * 0.04 / 12
        number_of_months += 1
    else:
        current_savings += portion_saved * annual_salary / 12 + current_savings * 0.04 / 12
        number_of_months += 1

print("Number of months:  ", number_of_months)