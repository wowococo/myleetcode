from leezy import solution, Solution
from leezy.assists import LinkedListContext


class Q083(Solution):
    @solution
    def deleteDuplicates(self, head):
        # 删除有序链表中的重复元素，和删除有序数组中的重复元素一样，首先想到的是使用双指针之快慢指针
        if not head:
            return 
        slow = fast = head
        while fast:
            # 正因为有序这个判断条件才这样写
            if fast.val != slow.val:
                slow.next = fast
                slow = slow.next

            fast = fast.next

        # 不要忘记将 slow 后面的链表截断
        slow.next = None

        return head


def main():
    q = Q083()
    q.set_context(LinkedListContext)
    q.add_case(q.case([1, 1, 2]))
    q.add_case(q.case([1,1,2,3,3]))
    q.run()


if __name__ == '__main__':
    main()
