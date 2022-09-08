from leezy import solution, Solution
from leezy.assists import ListNode

class Q141(Solution):
    @solution
    def hasCycle(self, head):
        # timeout way, this cannot test
        # s = set()
        # while head:
        #     if head in set():
        #         return True
        #     else:
        #         s.add(head)
        #     head = head.next
        # return False
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False

def main():
    q = Q141()
    make = ListNode.make_cycle_list
    q.add_case(q.case(make([3, 2, 0, -4], 1)).assert_equal(True))
    q.add_case(q.case(make([1, 2], 0)).assert_equal(True))
    q.add_case(q.case(make([1, 2], -1)).assert_equal(False))
    q.add_case(q.case(make([1], -1)).assert_equal(False))
    q.add_case(q.case(make([1], 0)).assert_equal(True))
    q.run()


if __name__ == '__main__':
    main()
