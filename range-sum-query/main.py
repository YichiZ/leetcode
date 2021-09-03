from typing import List

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        
# Need to hashmap
    def sumRange(self, left: int, right: int) -> int:
        return sum(self.nums[left:right+1])

if __name__=="__main__":
    nums = [-2, 0, 3, -5, 2, -1]

    obj = NumArray(nums)
    param_1 = obj.sumRange(0, 2)
    print(param_1)


