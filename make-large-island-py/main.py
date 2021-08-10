from typing import List


class Solution:
    def islandSize(self, grid: List[List[int]]) -> int:
        pass

    def largestIsland(self, grid: List[List[int]]) -> int:
        print(grid)


if __name__ == "__main__":
    sol = Solution()
    grid: List[List[int]] = [[1, 0], [1, 1]]
    res = sol.largestIsland(grid)
