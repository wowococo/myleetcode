from leezy import solution, Solution


class Q278(Solution):
    @solution
    def firstBadVersion(self, n):
        l, r = 1, n
        while l < r:
            mid = l + (r - l) // 2
            if isBadVersion(mid):
                r = mid
            else:
                l = mid + 1
        return l

def main():
    q = Q278()
    q.add_case(q.case(5))
    q.run()


if __name__ == '__main__':
    main()
