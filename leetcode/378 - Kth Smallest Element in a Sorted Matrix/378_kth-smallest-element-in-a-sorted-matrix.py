from leezy import solution, Solution
from bisect import bisect

class Q378(Solution):
    @solution
    def kthSmallest(self, matrix, k):
        l = matrix[0][0]
        r = matrix[-1][-1]
        while l < r:
            m = l + (r-l) // 2
            total = 0
            for row in matrix:
                total += bisect(row, m)
            if total >= k:
                r = m
            else:
                l = m + 1
        return l 




def main():
    q = Q378()
    q.add_case(q.case([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8))
    q.run()


if __name__ == '__main__':
    main()
