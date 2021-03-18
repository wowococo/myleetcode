from leezy import solution, Solution


class Q509(Solution):
    @solution
    def fib(self, n):
        if n == 1:
            return 1
        if n == 0:
            return 0
        return self.fib(n-1) + self.fib(n-2)


def main():
    q = Q509()
    q.add_case(q.case(2).assert_equal(1))
    q.add_case(q.case(3).assert_equal(2))
    q.add_case(q.case(4).assert_equal(3))
    q.run()


if __name__ == '__main__':
    main()
