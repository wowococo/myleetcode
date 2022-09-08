from leezy import solution, Solution
from heapq import heappush, heappop

class Q373(Solution):
    @solution
    def kSmallestPairs(self, nums1, nums2, k):
        heap = [(nums1[0]+nums2[0], 0, 0)]
        def push(i, j):
            if i < len(nums1) and j < len(nums2):
                heappush(heap, (nums1[i]+nums2[j], i, j))
        ans = []
        while heap and len(ans) < k:
            _, i, j = heappop(heap)
            ans.append([nums1[i], nums2[j]])
            push(i, j+1)
            if j == 0:
                push(i+1, 0)
        return ans

def main():
    q = Q373()
    q.add_case(q.case([1, 7, 11], [2, 4, 6], 3).assert_equal([[1,2],[1,4],[1,6]]))
    q.add_case(q.case([1, 1, 2], [1, 2, 3], 2).assert_equal([[1,1],[1,1]]))
    q.add_case(q.case([1, 2], [3], 3).assert_equal([[1,3],[2,3]]))
    
    q.run()


if __name__ == '__main__':
    main()
