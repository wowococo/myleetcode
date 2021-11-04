from leezy import solution, Solution


class Q309(Solution):
    @solution
    def maxProfit(self, prices):
        # 44ms 28.23%
        # dp[i][0] 表示第 i 天持有股票 (买入股票)
        # dp[i][1] 表示第 i 天持有股票 (没有买入)
        # dp[i][2] 表示第 i 天不持有股票 (没有卖出)
        # dp[i][3] 表示第 i 天不持有股票 (卖出股票)
        n = len(prices)
        dp = [[-float('inf')] * 4 for _ in range(n)]
        dp[0][0] = -prices[0]
        dp[0][2] = 0
        dp[0][3] = 0
        for i in range(1, n):
            dp[i][0] = dp[i-1][2] - prices[i]
            dp[i][1] = max(dp[i-1][0], dp[i-1][1])
            dp[i][2] = max(dp[i-1][3], dp[i-1][2])
            dp[i][3] =max(dp[i-1][0], dp[i-1][1]) + prices[i]
        
        return max(dp[n-1][2], dp[n-1][3])
            

    def max_profit(self, prices):
        pass
    
def main():
    q = Q309()
    q.add_case(q.case([1, 2, 3, 0, 2]))
    q.run()


if __name__ == '__main__':
    main()
