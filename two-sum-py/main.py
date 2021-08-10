from typing import List


class Solution:
    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in hashmap:
                return [hashmap[complement], i]
            else:
                hashmap[nums[i]] = i


if __name__ == "__main__":
    sol = Solution()
    nums: List[int] = [2, 7, 11, 15]
    target = 9
    res = sol.twoSum(nums, target)
    print(res)
