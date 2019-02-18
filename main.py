def month_calculator():
    print('How much does your dream home cost?')
    total_cost = float(input())

    down_payment = total_cost * .25

    c_savings = 0
    annual_salary = float(input('What is your annual salary?'))
    portionsaved = float(input('What % of your salary are you going to save?'))

    r = .04

    i = 0

    while c_savings < down_payment:
        monthly_savings = ((annual_salary * portionsaved) / 12)
        c_savings = (((c_savings * r / 12) + monthly_savings) + c_savings)
        print(c_savings)
        i += 1

    print("It will take you " + str(i) + " months to save up enough money.")


month_calculator()
