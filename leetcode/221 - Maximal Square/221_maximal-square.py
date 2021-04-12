from leezy import solution, Solution


class Q221(Solution):
    @solution
    def maximalSquare(self, matrix):
        # 88ms 73.68%
        # dp[i][j] 表示第 i 行，第 j 列以 matrix[i-1][j-1]为右下角的正方形的最大边长
        m, n = len(matrix), len(matrix[0])
        side_len = 0
        dp = [[0] * (n+1) for _ in range(m+1)]
        # for i in range(m+1):
        #     dp[i][0] = 0  # 不用写，上面初始化dp的时候是0
        # for j in range(n+1):
        #     dp[0][j] = 0  # 不用写，上面初始化dp的时候是0
        for i in range(1, m+1):
            for j in range(1, n+1):
                if matrix[i-1][j-1] == '1':
                    #              左边       ，上边，     左上角
                    dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1
                    side_len = max(side_len, dp[i][j])
        
        return side_len * side_len


def main():
    q = Q221()
    q.add_case(q.case([['1', '0', '1', '0', '0'], ['1', '0', '1', '1', '1'], ['1', '1', '1', '1', '1'], ['1', '0', '0', '1', '0']]).assert_equal(4))
    q.run()


if __name__ == '__main__':
    main()
