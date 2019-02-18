def month_calculator():
    print('How much does your dream home cost?')
    total_cost = float(input())

    down_payment = total_cost * .25

    current_savings = 0
    annual_salary = float(input('What is your annual salary?'))
    portion_saved = float(input('What % of your salary are you going to save each month?'))

    r = .04

    i = 0

    while current_savings < down_payment:
        monthly_savings = ((annual_salary * portion_saved) / 12)
        current_savings = (((current_savings * r / 12) + monthly_savings) + current_savings)
        print(current_savings)
        i += 1

    print("It will take you " + str(i) + " months to save up enough money.")


month_calculator()
