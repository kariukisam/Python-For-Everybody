#Program to prompt user for hours and rate and compute gross pay


hours = input('Enter the number of hours: ')
rate = input('Enter the rate per hour: ')

pay = float(hours) * float(rate)

rounded_pay = round(pay,1)
print('The pay is: ', rounded_pay)

