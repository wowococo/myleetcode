from leezy import solution, Solution


class Q069(Solution):
    @solution
    def mySqrt(self, x):
        l = 0
        r = x
        while l <= r:
            m = l + (r - l) // 2
            if m * m > x:
                r = m-1
            else:
                l = m + 1
        return l-1

def main():
    q = Q069()
    q.add_case(q.case(4).assert_equal(2))
    q.add_case(q.case(8).assert_equal(2))
    q.add_case(q.case(1).assert_equal(1))
    q.add_case(q.case(0).assert_equal(0))
    q.add_case(q.case(10).assert_equal(3))
    q.run()


if __name__ == '__main__':
    main()
