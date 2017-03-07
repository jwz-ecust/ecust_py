class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def addTwoNumbers(self, l1, l2):
        l3 = ListNode(0)
        c1, c2, c3 = l1, l2, l3
        s, carry = 0, 0
        while c3 is not None:
            v1 = c1.val if c1 is not None else 0
            v2 = c2.val if c2 is not None else 0
            carry, s = divmod(v1 + v2 + carry, 10)
            c3.val = s
            if c1 is not None:
                c1 = c1.next
            if c2 is not None:
                c2 = c2.next
            if c1 is not None or c2 is not None or carry == 1:
                c3.next = ListNode(0)
            c3 = c3.next
        return l3


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

tt = Solution()
l3 = tt.addTwoNumbers(l1, l2)
print(l3.val)
print(l3.next.val)
print(l3.next.next.val)
