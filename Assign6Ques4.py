'''Ques4-Write a Python function to check whether a string is a pangram or not. Note: Pangrams 
are words or sentences containing every letter of the alphabet at least once. For 
example: "The quick brown fox jumps over the lazy dog" '''
your_string=str(input("Please enter the string to be checked :---"))
#22105015

def is_pangram(your_string):
    alphabet = ''
    for letter in your_string.lower():
        if letter.isalpha() and letter not in alphabet:
            alphabet += letter
    alphabet = ''.join(sorted(alphabet))
    if alphabet == 'abcdefghijklmnopqrstuvwxyz':
        return "yes it is a pangram"
    else:
        return "no it is not a pangram"
print(is_pangram(your_string))
#Arnav Vikas Garg
