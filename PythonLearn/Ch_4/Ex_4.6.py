#Using a computepay function for the pay computation program

def computepay(hours, rate):
    if hours > 40.0:
        overtime_pay = (hours - 40) *1.5 *rate
        pay = 40 * rate
        total_pay = overtime_pay + pay

    else:
        total_pay = hours  * rate

    return total_pay

hours = input("Enter the number of hours: ")
rate = input("Enter the rate per hour: ")

try:
    hours = float(hours)
    rate = float(rate)
    print("The pay is:", computepay(hours, rate))

except:
    print("Error, please enter a numeric value")


