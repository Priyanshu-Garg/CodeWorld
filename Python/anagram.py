# An anagram is a word or phrase that's formed by rearranging the letters of another word or phrase.
# For example, the letters that make up "Dormitory" turns into the anagram "dirty room"

#anagram check function
def anagram_check(first_string, second_string):
    string1 = []
    string2 = []
    for i in first_string:
        if i.isalpha():
            string1.append(i.lower())
        else:
            continue
    for i in second_string:
        if i.isalpha():
            string2.append(i.lower())
        else:
            continue
    if sorted(string1) == sorted(string2):
        print("The strings are anagram.")
    else:
        print("The strings are not anagram.")


#Take the first input string from the user
first_string = input("Enter first string : ")

#Take the second input string from the user
second_string = input("Enter second string : ")

#call the anagram check function and send both the inputted string as parameters.
anagram_check(first_string, second_string)