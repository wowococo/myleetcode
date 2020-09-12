from leezy import solution, Solution


class Q070(Solution):
    @solution
    def climbStairs(self, n):
        # f[i] = climbStairs[n]
        f = [0] * (n + 1)
        f[0] = 1
        f[1] = 1
        
        # f[i] = f[i - 2] + f[i - 1] 斐波那列序列
        for i in range(2, n + 1):
            f[i] = f[i - 2] + f[i - 1]
        return f[n]



def main():
    q = Q070()
    q.add_case(q.case(2).assert_equal(2))
    q.add_case(q.case(3).assert_equal(3))
    q.run()


if __name__ == '__main__':
    main()
