# a function to count a specific letter in a a word

def count(word, letter):
    times = 0
    for char in word:
        if char == letter:
            times = times + 1

    return times

word = input("Input a word or sentence: ")
letter = input("Input the letter to count: ")
try:
    word = str(word)
    letter = str(letter)

    print("The number of times the letter appears is: \n", count(word,letter))

except:
    print("Input a non-integer value")

