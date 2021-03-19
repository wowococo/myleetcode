from leezy import solution, Solution


class Q509(Solution):
    @solution
    def fib(self, n):
        # 重叠子问题
        if n == 1:
            return 1
        if n == 0:
            return 0
        return self.fib(n-1) + self.fib(n-2)
    
    @solution
    def fib_better(self, n):
        memo = [0] * (n+1)
        return self.f(memo, n)
    
    def f(self, memo, n):
        if n == 1: return 1
        if n == 0: return 0
        if memo[n] != 0:
            return memo[n]
        memo[n] = self.f(memo, n-1) + self.f(memo, n-2)
        return memo[n]
    


def main():
    q = Q509()
    q.add_case(q.case(2).assert_equal(1))
    q.add_case(q.case(3).assert_equal(2))
    q.add_case(q.case(4).assert_equal(3))
    q.run()


if __name__ == '__main__':
    main()
