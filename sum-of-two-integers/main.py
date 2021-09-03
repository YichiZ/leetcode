class Solution:
    def getSum(self, a: int, b: int) -> int:
        # Substraction Table
        # a b | s b
        # 0 0 | 0 0
        # 1 0 | 1 0
        # 0 1 | 1 1
        # 1 1 | 0 0
        if a ^ b < 0:
            negative = False
            if abs(b) > abs(a):
                temp = a
                a = b
                b = temp

            if a < 0:
                negative = True
            a = abs(a)
            b = abs(b)

            while(b != 0):
                sum = a ^ b
                borrow = (~a) & b

                a = sum
                b = borrow << 1

            if negative:
                return -a
            else:
                return a

        # Addition Table
        # a b | s c
        # 0 0 | 0 0
        # 1 0 | 1 0
        # 0 1 | 1 0
        # 1 1 | 0 1
        else:
            while (b != 0):
                sum = a ^ b
                carry = a & b

                a = sum
                b = carry << 1

        return a


if __name__ == "__main__":
    sol = Solution()
    res = sol.getSum(-2, 1)
    print(res)
