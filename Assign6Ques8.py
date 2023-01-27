'''Write a Python class to find the three elements that sum to zero from a set of n real 
numbers. 
Input array: [-25, -10, -7, -3, 2, 4, 8, 10]
Output: [[-10, 2, 8], [-7, -3, 10]]'''
#22105015
class SumZero:
    def __init__(self,nums):
        self.nums = nums

    def sumZero(self):
        result = []
        for i in range(len(self.nums)):
            for j in range(i + 1, len(self.nums)):
                for k in range(j + 1, len(self.nums)):
                    if(self.nums[i] + self.nums[j] + self.nums[k] == 0):
                        result.append([self.nums[i], self.nums[j], self.nums[k]])
        return result

nums =[]
n = int(input("Enter number of elements : "))
  
# iterating till the range
for i in range(0, n):
    ele = int(input())
#22105015  
    nums.append(ele) # adding the element    
sz = SumZero(nums)
print(sz.sumZero())
  

