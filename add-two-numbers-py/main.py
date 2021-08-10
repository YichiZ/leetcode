
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        h1 = l1
        h2 = l2
        r1 = ListNode(0)
        s1 = r1
        while h1 != None or h2 != None or carry != 0:
            left = h1 and h1.val or 0
            right = h2 and h2.val or 0
            sum = left + right + carry
            carry = 0
            if sum >= 10:
                sum = sum % 10
                carry = 1

            s1.next = ListNode(sum)
            s1 = s1 and s1.next or None
            h1 = h1 and h1.next or None
            h2 = h2 and h2.next or None

        return r1.next


if __name__ == "__main__":
    l1 = ListNode(2)
    l2 = ListNode(4)
    l3 = ListNode(3)
    l1.next = l2
    l2.next = l3

    r1 = ListNode(5)
    r2 = ListNode(6)
    r3 = ListNode(6)
    r1.next = r2
    r2.next = r3

    sol = Solution()
    res = sol.addTwoNumbers(l1, r1)
    print(res)
