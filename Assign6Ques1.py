'''Ques1. Write a Python function to check whether a number is perfect or not. According to 
Wikipedia : In number theory, a perfect number is a positive integer that is equal to the 
sum of its proper positive divisors, that is, the sum of its positive divisors excluding the 
number itself (also known as its aliquot sum). Equivalently, a perfect number is a 
number that is half the sum of all of its positive divisors (including itself).'''
Num = int(input(" Please Enter any Number: "))
Sum = 0
for i in range(1, Num):
    if(Num % i == 0):
        Sum = Sum + i
if (Sum == Num):
    print(" %d is a Perfect Number" %Num)
else:
    print(" %d is not a Perfect Number" %Num)
#22105015
#by-arnav vikas garg
