from leezy import solution, Solution
import math

class Q875(Solution):
    @solution
    def minEatingSpeed(self, piles, H):
        def possible(k):
            return sum((p-1) // k + 1 for p in piles) <= H

        lo, hi = 1, max(piles)
        while lo < hi:
            m = lo + (hi - lo) // 2
            if possible(m):
                hi = m
            else:
                lo = m + 1
        return lo


def main():
    q = Q875()
    q.add_case(q.case([3, 6, 7, 11], 8))
    q.run()


if __name__ == '__main__':
    main()
