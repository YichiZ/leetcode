from typing import List

# Incomplete


class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        arr.sort()
        while len(arr) != 0:
            isEven = False
            num = arr[0]
            double = num * 2
            if num % 2 == 0:
                isEven = True
                half = num / 2
            if double in arr:
                index = arr.index(double)
                del arr[index]
                del arr[0]
            elif isEven and half in arr:
                index = arr.index(half)
                del arr[index]
                del arr[0]
            else:
                return False
        return True


if __name__ == "__main__":
    arr = [2, 4, 0, 0, 8, 1]
    sol = Solution()
    print(sol.canReorderDoubled(arr))
