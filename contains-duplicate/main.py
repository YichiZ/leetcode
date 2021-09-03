from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}

        for i in range(len(nums)):
            if nums[i] in hashmap.keys():
                return True

            hashmap[nums[i]] = ""

        return False


if __name__ == "__main__":
    sol = Solution()
    res = sol.containsDuplicate([1, 2, 3, 4])
    print(res)
