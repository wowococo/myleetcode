from leezy import solution, Solution


class Q062(Solution):
    @solution
    def uniquePaths(self, m, n):
        # dp[i][j] 表示到达 grid[i][j] 的路径
        # dp[i][j] = dp[i][j-1] + dp[i-1][j]
        # 28ms 91.83%
        dp = [[0] * n for _ in range(m)]
        for j in range(n):
            dp[0][j] = 1
        for i in range(m):
            dp[i][0] = 1
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i][j-1] + dp[i-1][j]
                
                
        return dp[m-1][n-1]


def main():
    q = Q062()
    q.add_case(q.case(3, 7).assert_equal(28))
    q.add_case(q.case(3, 2).assert_equal(3))
    q.add_case(q.case(7, 3).assert_equal(28))
    q.add_case(q.case(3, 3).assert_equal(6))
    q.run()


if __name__ == '__main__':
    main()
