from leezy import solution, Solution


class Q279(Solution):
    @solution
    def numSquares(self, n):
        # dp[i] 表示数字 i 的完全平方数的最小数量
        # dp[i] = min(i, dp[i-j*j] + 1)   
        # TLE 514/588     
        dp = [0] * (n + 1)
        dp[1] = 1
        for i in range(2, n+1):
            dp[i] = i
            for j in range(1, i):
                if i >= j * j:   # if i >= j **2 ---> 502/588
                    dp[i] = min(dp[i], dp[i-j*j]+1)

        return dp[n]

    @solution
    def num_squares(self, n):
        # 改写成 while 循环, 4012ms, 40.74%
        dp = [0] * (n + 1)
        dp[1] = 1
        for i in range(2, n+1):
            dp[i] = i
            j = 1
            while i >= j*j:
                dp[i] = min(dp[i], dp[i-j*j]+1)
                j += 1

        return dp[n]


def main():
    q = Q279()
    q.add_case(q.case(12).assert_equal(3))
    q.add_case(q.case(13).assert_equal(2))
    q.run()


if __name__ == '__main__':
    main()
