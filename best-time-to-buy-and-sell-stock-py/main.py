from typing import List
import math


class Solution:
    def maxProfit2(self, prices: List[int]) -> int:
        maxProfit = 0
        for i in range(len(prices)):

            for j in range(i + 1, len(prices)):
                if prices[j] > prices[i]:
                    profit = prices[j] - prices[i]

                    if profit > maxProfit:
                        maxProfit = profit

        return maxProfit

    # Go to a minima and check for the maximum until the next minimum
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = math.inf
        maxProfit = 0

        for i in range(len(prices)):
            if prices[i] < minPrice:
                minPrice = prices[i]

            profit = prices[i] - minPrice
            if profit > maxProfit:
                maxProfit = profit

        return maxProfit


if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]
    sol = Solution()
    res = sol.maxProfit(prices)
    print(res)
