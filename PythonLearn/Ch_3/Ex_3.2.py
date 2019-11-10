# Rewriting pay computation using error handling for increased rate for work hours above 40

hours = input('Enter the number of hours: ')
rate = input('Enter the rate per hour: ')

try:
    if float(hours) > 40.0:
        overtime_pay = (float(hours) - 40) * 1.5 * float(rate)
        pay = 40.0 * float(rate)
        total_pay = overtime_pay + pay

    else:
        total_pay = float(hours) * float(rate)

    rounded_pay = round(total_pay, 2)
    print('The pay is:', rounded_pay)

except:
    print("Error, please enter numeric input")



