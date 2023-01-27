'''Ques5-Write a Python function that accepts a hyphen-separated sequence of words as input 
and prints the words in a hyphen-separated sequence after sorting them alphabetically. 
Sample Items : green-red-yellow-black-white
Expected Result : black-green-red-white-yellow'''
def sort_hyphen(x):
    z= x.split('-')
    z.sort()
    return '-'.join(z)                            #22105015
checkstring =str(input("Please enter sequence of words to be arranged with hyphen ::"))
print(sort_hyphen(checkstring))
#22105015
#Arnav 
