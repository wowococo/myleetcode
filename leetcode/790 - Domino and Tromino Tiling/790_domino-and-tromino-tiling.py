from leezy import solution, Solution


class Q790(Solution):
    @solution
    def numTilings(self, N):
        k_mod = 1000000007
        dp = [[0] * 2 for _ in range(N + 1)]
        dp[0][0] = dp[1][0] = 1
        for i in range(2, N+1):
            dp[i][0] = (dp[i-1][0] + dp[i-2][0] + 2 * dp[i-1][1]) % k_mod
            dp[i][1] = (dp[i-2][0] + dp[i-1][1]) % k_mod
        return dp[N][0]


def main():
    q = Q790()
    q.add_case(q.case(3).assert_equal(5))
    q.run()

if __name__ == '__main__':
    main()
