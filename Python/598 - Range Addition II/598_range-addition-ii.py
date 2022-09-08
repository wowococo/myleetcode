from leezy import solution, Solution


class Q598(Solution):
    @solution
    def maxCount(self, m, n, ops):
        if not ops:
            return m * n
        a = b = 10000
        for p in ops:
            a0, b0 = p
            a = min(a, a0)
            b = min(b, b0)
        return a * b



def main():
    q = Q598()
    q.add_case(q.case(3, 3, [[2, 2], [3, 3]]))
    # q.add_case(q.case(3, 3, [[2, 3], [1, 2]]))
    q.run()

if __name__ == '__main__':
    main()
