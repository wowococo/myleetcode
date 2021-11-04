from leezy import solution, Solution
from leezy.assists import ListNode

class Q142(Solution):
    @solution
    def detectCycle(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                break
        else:
            return None
    
        cursor = head
        while cursor is not slow:
            cursor = cursor.next
            slow = slow.next
            print(cursor.val)
        return cursor

def main():
    q = Q142()
    make = ListNode.make_cycle_list
    q.add_case(q.case(make([3, 2, 0, -4], 1)))
    q.add_case(q.case(make([1, 2], 0)))
    q.run()


if __name__ == '__main__':
    main()
