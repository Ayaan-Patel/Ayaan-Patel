# This program asks the user for their hourly pay and hours worked. It then calculates a net pay with a 22% tax deduction, which it then rounds off to 2 decimal points

hourly_pay = float(input())

hours_worked = float(input())

net_payA = hourly_pay * hours_worked / 100 * 78

net_payB = "${:,.2f}".format(net_payA)

print("After taxes, your income is", net_payB)
