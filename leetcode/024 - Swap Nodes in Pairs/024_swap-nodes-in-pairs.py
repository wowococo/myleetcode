from leezy import solution, Solution
from leezy.assists import LinkedListContext, ListNode

class Q024(Solution):
    @solution
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(24)
        dummy.next = head
        pre = dummy
        while True:
            if head is None or head.next is None:
                break
            # swap two nodes need a pre and after 
            after = head.next.next
            pre.next = head.next
            pre.next.next = head
            head.next = after
            pre = head
            head = after
        return dummy.next
            
def main():
    q = Q024()
    q.set_context(LinkedListContext)
    make = ListNode.make_linked_list
    q.add_case(q.case([1, 2, 3, 4]).assert_equal(make([2, 1, 4, 3])))
    q.add_case(q.case([1, 2, 3]).assert_equal(make([2, 1, 3])))
    q.add_case(q.case([1, 2]).assert_equal(make([2, 1])))
    q.add_case(q.case([1]).assert_equal(make([1])))
    q.run()

if __name__ == '__main__':
    main()
