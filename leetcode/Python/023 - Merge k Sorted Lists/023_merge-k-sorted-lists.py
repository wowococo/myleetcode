from leezy import solution, Solution
from leezy.assists import ListNode

class Q023(Solution):
    # 优先级队列 solution1
    @solution
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:  
        import heapq
        heap = []
        if not lists: return 
        dummy = tail = ListNode(0)
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap,(lists[i].val, i))

        while heap:
            v, idx = heappop(heap)
            tail.next = ListNode(v)
            tail = tail.next
            # lists[idx]一定是非 NoneType
            if lists[idx].next:
                heappush(heap, (lists[idx].next.val, idx))
                lists[idx] = lists[idx].next

        return dummy.next

    # 分而治之，有递归, 用到21题（合并两个升序链表）
    @solution
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:  
        return self.merge(lists, 0, len(lists) - 1)
    
    # l, r 均是 lists 0的索引, lists[l], lists[r] 均是链表
    def merge(self, lists, l, r):
        if l > r: return 
        if l == r: return lists[l]
        if l + 1 == r: return self.mergeTwoLists(lists[l], lists[r])
        if l < r:
            m = l + (r - l) // 2
            l1 = self.merge(lists, l, m)
            l2 = self.merge(lists, m+1, r)
            return self.mergeTwoLists(l1, l2)

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = tail = ListNode(0)
        while l1 and l2:
            if l1.val > l2.val:
                l1, l2 = l2, l1
            tail.next = l1
            l1 = l1.next
            tail = tail.next
        if l1: tail.next = l1
        if l2: tail.next = l2
        return dummy.next
        

def main():
    q = Q023()
    q.add_case(q.case([[1, 4, 5], [1, 3, 4], [2, 6]]))
    q.run()

if __name__ == '__main__':
    main()
