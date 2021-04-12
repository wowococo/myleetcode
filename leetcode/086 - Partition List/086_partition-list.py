from leezy import solution, Solution
from leezy.assists import LinkedListContext, ListNode


class Q086(Solution):
    @solution
    def partition(self, head, x):
        # 32ms 98.22%  
        # 先分隔成小大两个链表，然后将两个连接起来
        if not head or not head.next:
            return head
        small = small_dummy = ListNode(0)
        big = big_dummy = ListNode(0)
        while head:
            if head.val < x:
                small.next = head
                small = small.next
            else:
                big.next = head
                big = big.next
            head = head.next
                
        small.next = big_dummy.next
        # 避免造成环形链表,环形链表不仅不正确，还超时
        big.next = None
        return small_dummy.next
    


def main():
    q = Q086()
    q.set_context(LinkedListContext)
    q.add_case(q.case([1, 4, 3, 2, 5, 2], 3))
    q.run()


if __name__ == '__main__':
    main()
