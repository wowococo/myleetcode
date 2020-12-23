from leezy import solution, Solution


class Q668(Solution):
    @solution
    def findKthNumber(self, m, n, k):
        # 732 ms faster than 81.02%, 14.8 MB less than 5.97%
        l, r = 1, m * n + 1
        while l < r:
            mid = l + (r - l) // 2
            total = 0
            for i in range(1, m + 1):
                total += min(mid // i, n)
                if total >= k:
                    break
            if total >= k:
                r = mid
            else:
                l =  mid + 1
        return l


def main():
    q = Q668()
    q.add_case(q.case(3, 3, 5).assert_equal(3))
    q.add_case(q.case(2, 3, 6).assert_equal(6))
    q.run()


if __name__ == '__main__':
    main()
