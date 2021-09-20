from leezy import solution, Solution


class Q322(Solution):
    @solution
    def coinChange(self, coins, amount):
        # 二维 dp, dp[i][j] 表示用 i 种类型的硬币凑成总金额 j。
        # dp[i][j] = min(dp[i][j], dp[i-1][j-k*coin_i] + k)
        #          = min(dp[i][j], dp[i][j-coin_i] + 1)
        # TLE 135/188
        dp = [float('inf')] * (amount+1)
        dp[0] = 0
        for coin in coins:
            for i in range(amount-coin, -1, -1):
                if dp[i] != float('inf'):
                    k = 1
                    while k * coin + i <= amount:
                        dp[i+k*coin] = min(dp[i+k*coin], dp[i] + k)
                        k += 1

        return dp[amount] if dp[amount] != float('inf') else -1 


    @solution
    def CoinChange(self, coins, amount):
        # 一维 dp,  由第二种，可得出 dp[j] = min(dp[j], dp[j-coin_i] + 1)
        # dp[i] 表示凑成 amount i 的最小硬币数。
        # 1056ms 65.32%
        dp = [float('inf')] * (amount+1)
        dp[0] = 0
        for coin in coins:
            for i in range(coin, amount+1):
                    dp[i] = min(dp[i], dp[i-coin]+1)
        
        return dp[amount] if dp[amount] != float('inf') else -1

    
    @solution
    def coin_change_memo(self, coins, amount):
        # 1408ms 22.53%
        memo = {}
        coins = sorted(coins)
        ans = self.dfs_memo(amount, coins, memo)
        return ans if ans != float('inf') else -1

    def dfs_memo(self, amount, coins, memo):
        if amount == 0:
            return 0
        if amount in memo:
            return memo[amount]
        ans = float('inf')
        for coin in coins:
            if coin > amount:
                break  
            ans = min(ans, self.dfs_memo(amount-coin, coins, memo)+1)

        memo[amount] = ans

        return ans

    @solution
    def coin_change(self, coins, amount):
        # dfs + 剪枝 TLE 39/188
        coins = sorted(coins, reverse=True)
        ans = float('inf')
        ans = self.dfs(0, amount, coins, 0, ans)
        return -1 if ans == float('inf') else ans

    def dfs(self, s, amount, coins, count, ans):
        coin = coins[s]
        # last element
        if s == len(coins)-1:
            if amount % coin == 0:
                ans = min(ans, count + amount // coin)
        else:
            k = amount // coin
            while k >= 0 and count + k < ans:
                ans = self.dfs(s+1, amount-k*coin, coins, count+k, ans)
                k -= 1
        return ans

    @solution
    def coin_change_prune(self, coins, amount):
        # now TLE 39/188
        least = [float('inf')]
        coins = sorted(coins, reverse=True)
        self.dfs_prune_boilerplate(coins, 0, amount, 0, least)
        return least[0] if least[0] != float('inf') else -1

    def dfs_prune_boilerplate(self, coins, s, amount, count, least):
        if s >= len(coins):
            if amount == 0:
                least[0] = min(least[0], count)
            return
        c = coins[s]
        for k in range(amount // c, -1, -1):
            if count + k >= least[0]:
                break
            self.dfs_prune_boilerplate(
                coins, s+1, amount - k*c, count+k, least)

def main():
    q = Q322()
    q.add_case(q.case([1, 2, 5], 11).assert_equal(3))
    q.add_case(q.case([2], 3).assert_equal(-1))
    q.add_case(q.case([1], 0).assert_equal(0))
    q.add_case(q.case([1], 1).assert_equal(1))
    q.add_case(q.case([1], 2).assert_equal(2))
    q.run()


if __name__ == '__main__':
    main()
