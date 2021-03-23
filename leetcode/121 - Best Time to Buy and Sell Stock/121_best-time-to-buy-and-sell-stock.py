from leezy import solution, Solution


class Q121(Solution):
    @solution
    def maxProfit(self, prices):
        if len(prices) < 2:
            return 0
        dp = prices[0]
        ans = 0
        for x in prices[1:]:
            dp = min(dp, x)
            ans = max(ans, x-dp)
        return ans


    @solution
    def maxProfit(self, prices):
        # TLE,所以要思考如何将o(n^2)的时间复杂度转成o(n)的
        n = len(prices)
        # dp[i] 表示以 prices[i] 那个价格卖出的最大收益
        dp = [0] * n
        for i in range(n):
            for j in range(i):
                if prices[i] > prices[j]:
                    dp[i] = max(dp[i], prices[i]-prices[j])
        
        return max(dp)
    
    @solution
    def maxProfit(self, prices):
        # TLE
        n = len(prices)
        # dp[i][j] 表示在第i天买入，第j天卖出
        dp = [[0] * (n+1) for _ in range(n+1)]
        for j in range(2, n+1):
            for i in range(1, j+1):
                dp[i][j] = prices[j-1] - prices[i-1]
        return max(map(max, dp))
    

def main():
    q = Q121()
    q.add_case(q.case([7, 1, 5, 3, 6, 4]).assert_equal(5))
    q.add_case(q.case([7,6,4,3,1]).assert_equal(0))
    q.add_case(q.case([1,2]).assert_equal(1))
    q.run()


if __name__ == '__main__':
    main()
