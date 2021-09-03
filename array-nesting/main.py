from typing import List


class Solution:
    def __init__(self) -> None:
        self.visited = set()

    def arrayNesting(self, nums: List[int]) -> int:
        max = 0
        for i in range(len(nums)):
            if i in self.visited:
                continue
            count = self.countCycle(i, nums)
            if (count > max):
                max = count

        return max

    def countCycle(self, index, nums):
        current = index
        count = 0
        while True:
            if current in self.visited:
                return count
            else:
                self.visited.add(current)
                current = nums[current]
                count += 1


if __name__ == '__main__':
    sol = Solution()
    sol.arrayNesting([5, 4, 0, 3, 1, 6, 2])
