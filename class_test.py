import pygame

class Numbers():
    def __init__(self, total):
        self.total = total
        
    def add(self, nums):
        for num in nums:
            self.total += num
        return self.total

    def add_copy(self, nums):
        self.total = self.add(nums)
        return self.total
            
total = 0
nums = [1, 2, 3]
num_function = Numbers(total)
total = num_function.add_copy(nums)
print(total)
