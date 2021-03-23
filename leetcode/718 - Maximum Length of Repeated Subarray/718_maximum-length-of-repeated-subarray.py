from leezy import solution, Solution


class Q718(Solution):
    @solution
    def findLength(self, A, B):
        # dp[i][j] 表示以A[i-1]，B[j-1]为结尾的子数组的最长公共子数组的长度
        # i, j 表示两个子数组的长度
        m, n = len(A), len(B)
        dp = [[-1] * (n+1) for _ in range (m+1)]
        for i in range(m+1):
            dp[i][0] = 0
        for j in range(n+1):
            dp[0][j] = 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                if A[i-1] == B[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = 0
            
        return max(map(max, dp))

def main():
    q = Q718()
    q.add_case(q.case([1, 2, 3, 2, 1], [3, 2, 1, 4, 7]))
    q.run()


if __name__ == '__main__':
    main()
