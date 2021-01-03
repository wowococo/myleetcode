from leezy import solution, Solution
from leezy.assists import ListNode, LinkedListContext

class Q445(Solution):
    @solution
    def addTwoNumbers(self, l1, l2):
        # 84 ms faster than 52.88%, 14.7 MB less than 12.06%
        s1, s2 = [], []
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        while l2:
            s2.append(l2.val)
            l2 = l2.next
        carry = 0
        node = None
        while s1 and s2:
            carry, value = divmod(s1.pop()+s2.pop()+carry, 10)
            tail = ListNode(value)
            tail.next = node
            node = tail
        s = s1 or s2
        while s:
            carry, value = divmod(s.pop()+carry, 10)
            tail = ListNode(value)
            tail.next = node
            node = tail
        if carry:
            tail = ListNode(carry)
            tail.next = node
            node = tail
        return node
    
    @solution
    def addTwoNumbers2(self, l1, l2):
        # 80 ms, more 
        stack1, stack2 = [], []
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
        carry = 0
        head = None  
        while stack1 or stack2 or carry:
            s = (stack1.pop() if stack1 else 0) + (stack2.pop() if stack2 else 0) + carry
            carry, v = divmod(s, 10)
            n = ListNode(v)
            n.next = head
            head = n
        return head

def main():
    q = Q445()
    q.set_context(LinkedListContext)
    make = LinkedListNode.make_linked_list
    q.add_case(q.case([7, 2, 4, 3], [5, 6, 4]).assert_equal(make([7, 8, 0, 7])))
    q.add_case(q.case([9, 4, 4, 3], [5, 6, 4]).assert_equal(make([1, 0, 0, 0, 7])))
    # q.add_case(q.case([9, 4, 4, 3], [5, 6, 4]))
    # q.add_case(q.case([0], [9, 9, 9]))
    q.add_case(q.case([0], [9, 9, 9]).assert_equal(make([9, 9, 9])))
    q.add_case(q.case([1], [9, 9, 9]).assert_equal(make([1, 0, 0, 0])))
    q.run()

if __name__ == '__main__':
    main()
