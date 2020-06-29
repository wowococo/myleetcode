from leezy import solution, Solution
from leezy.assists import LinkedListContext, LinkedListNode


class Q002(Solution):
    @solution
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        dummy = tail = LinkedListNode(0)
        while l1 or l2 or carry:
            s = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            tail.next = LinkedListNode(s % 10)
            tail = tail.next
            carry = s // 10
            l1 = l1.next if l1 else None  # NoneType has no attribute next, val
            l2 = l2.next if l2 else None
        return dummy.next

def main():
    q = Q002()
    q.set_context(LinkedListContext)
    make = LinkedListNode.make_linked_list
    q.add_case(q.case([5], [5]).assert_equal(make([0, 1])))
    q.add_case(q.case([2, 4, 3], [5, 6, 4]).assert_equal(make([7, 0, 8])))
    q.run()

if __name__ == '__main__':
    main()
