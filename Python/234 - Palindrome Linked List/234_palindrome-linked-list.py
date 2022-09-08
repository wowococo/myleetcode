from leezy import solution, Solution
from leezy.assists import LinkedListContext
import copy

class Q234(Solution):
    @solution
    def isPalindrome(self, head):
        def reverse(head):
            pre, cur = None, head
            while cur:
                tmp = cur.next
                cur.next = pre
                pre = cur
                cur = tmp
            return pre
        tail = reverse(copy.deepcopy(head))
        while head:
            if head.val != tail.val:
                return False
            head, tail = head.next, tail.next
        return True

    @solution
    def isPalindrome2(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # 结点有奇数个，此时slow恰好在最中间位置，取右小半边，将slow向右移动一步
        if fast != None:
            slow = slow.next
        
        # 反转右边链表
        slow = self.reverse(slow)
        fast = head
        while slow:
            if fast.val != slow.val:
                return False
            slow, fast = slow.next, fast.next
        return True

    def reverse(self, head):
        pre, cur = None, head
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre





def main():
    q = Q234()
    q.set_context(LinkedListContext)
    q.add_case(q.case([1, 1, 2, 1]))
    q.run()


if __name__ == '__main__':
    main()
