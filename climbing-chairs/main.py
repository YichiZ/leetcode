class Solution:
    def __init__(self) -> None:
        self.hashmap = {1: 1, 2: 2}

    def climbStairs(self, n: int) -> int:
        # if n = 1: 1
        # if n = 2: 1-1, 2
        # if n = 3: 1-1-1, 2-1, 1-2
        # if n = 4: 1-1-1-1, 1-1-2, 2-1-1, 1-2-1, 2-2

        if n in self.hashmap.keys():
            return self.hashmap[n]

        count = 0
        count += self.climbStairs(n - 1) + self.climbStairs(n - 2)

        self.hashmap[n] = count

        return self.hashmap[n]


if __name__ == "__main__":
    sol = Solution()
    res = sol.climbStairs(50)
    print(res)
