# Program to repeatedly read a number until done is entered

count = 0
total = 0
print
while True:
    value = input("Enter a number or type done to end: ")

    if value == "done":
        break

    else:
        try:
            value = float(value)
            total = total + value
            count = count + 1
            average = total / count

        except:
            print("Invalid input. Input an integer!")



print("\nThe total is: ", total, "\nThe count is: ", count, "\nThe average is: ", average)




