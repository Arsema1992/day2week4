#Write a function that takes a string and outputs a strings of 1's and 0's 
#where vowels become 1's and non-vowels become 0's.
#All non-vowels including non alpha characters (spaces,commas etc.) should be included.


def vowel_one(string):
    vowels = "aeiou"
    result = ""
    for char in string:
        if char.lower() in vowels:
            result += "1"
        else:
            result += "0"
    return result





