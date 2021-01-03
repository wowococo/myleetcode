from leezy import solution, Solution
from leezy.assists import ListNode

class Q023(Solution):
    @solution
    def mergeKLists(self, lists):
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
        
        


def main():
    q = Q023()
    q.add_case(q.case([[1, 4, 5], [1, 3, 4], [2, 6]]))
    q.run()

if __name__ == '__main__':
    main()
