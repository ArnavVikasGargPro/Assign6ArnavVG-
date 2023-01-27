'''Ques2:--Write a Python function that checks whether a passed string is palindrome or not. Note: 
A palindrome is a word, phrase, or sequence that reads the same backward as forward, 
e.g., madam or nurses run.'''
def isPalindrome(pas):
    return pas ==pas[::-1]
pas = str(input("Please enter the word to be checked for palindrome or not :- "))
check = isPalindrome(pas)
#22105015
if check:
    print("Yes,it is a palindrome")
else:
    print("No,it is not a palindrome")
#Arnav Vikas Garg
