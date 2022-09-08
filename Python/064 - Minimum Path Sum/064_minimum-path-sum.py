from leezy import solution, Solution


class Q064(Solution):
    @solution
    def minPathSum(self, grid):
        # dp[i][j] 表示以 grid[i][j] 为结尾的最小数字总和
        # dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        # 48ms 60.85%
        m, n = len(grid), len(grid[0])
        if n < 1:
            return 0
        dp = [[-1] * n for _ in range(m)]

        dp[0][0] = grid[0][0]
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        for j in range(1, n):
            dp[0][j] = dp[0][j-1] + grid[0][j]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        
        return dp[m-1][n-1]

    @solution
    def Minpathsum(self, grid):
        # 48ms, 60.85%
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])  
        # start point is  (1, 1) and end point is (m, n)
        # dp[i][j] means min cost from left-top to grid(i-1,j-1)
        dp = [[float('inf')]*(n+1) for _ in range(m+1)]
        dp[1][0] = 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i-1][j-1]

        return dp[m][n]
        

    @solution
    def min_path_sum(self, grid):
        # 32ms, 99.16%, 压缩成一维dp，只包含列的 dp。压缩为行的一维 dp 是错误的，因为行覆盖不到右下角
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        dp = [float('inf')] * (n+1)
        dp[1] = 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                dp[j] = min(dp[j], dp[j-1]) + grid[i-1][j-1]

        return dp[-1] 


def main():
    q = Q064()
    q.add_case(q.case([[1, 3, 1], [1, 5, 1], [4, 2, 1]]).assert_equal(7))
    q.add_case(q.case([[1,2,3],[4,5,6]]).assert_equal(12))
    q.add_case(q.case([[1,2],[1,1]]).assert_equal(3))
    q.run()


if __name__ == '__main__':
    main()
