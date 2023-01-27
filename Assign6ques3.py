'''Ques3. Write a Python function that prints out the first n rows of Pascal's triangle. Note:
Pascal's triangle is an arithmetic and geometric figure first imagined by Blaise Pascal.'''
def solve(n):
   for i in range(n+1):
      for j in range(n-i):
         print(' ', end='')
#22105015
      C = 1
      for j in range(1, i+1):
         print(C, ' ', sep='', end='')
         C = C * (i - j) // j
      print()

n =int(input("Please enter the no of rows of pascal triangle you want to print::-"))
solve(n)
#22105015
