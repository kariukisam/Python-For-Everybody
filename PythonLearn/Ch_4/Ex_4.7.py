# Using a computegrade function fot the grade program

def computegrade(score):
    if 0 <= score < 0.6:
        print("F")

    elif 0.6 <= score < 0.7:
        print("D")

    elif 0.7 <= score < 0.8:
        print("C")

    elif 0.8 <= score < 0.9:
        print("B")

    elif 0.9 <= score <= 1.0:
        print("A")

    else:
        print("Bad Score")

while 1:
    score = input("Enter the score between 0 and 1: ")

    try:
        score = float(score)
        computegrade(score)

    except:
        print("Bad score")
