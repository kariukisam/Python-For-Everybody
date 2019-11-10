# Program that prompts for a list of numbers and prints out the maximum and minimum

minimum = None
maximum = None
#count = 0
#list = []
while True:
    value = input("Enter a number or type done when done: ")

    if value == "done":
        break

    else:
        try:
            value = float(value)
            #list[count] = value
            #count = count + 1
            #minimum = min(list)
            #maximum = max(list)
            #sum = sum(list)

            if minimum is None  or value < minimum:
                minimum = value

            if maximum is None  or value > maximum:
                maximum = value

        except:
            print("Ivalid input. Input an integer")

print("\nThe minimum number is:", minimum, "\nThe maximum number is:", maximum)