from leezy import solution, Solution


class Q198(Solution):
    @solution
    def rob(self, nums) -> int:
        # 28ms  
        n = len(nums)
        dp = [0] * (n+2)
        for i in range(n-1, -1, -1):
            dp[i] = max(dp[i+1], dp[i+2]+nums[i])
        return dp[0]  # or return max(dp)
    
    @solution
    def rob_substraction(self, nums):
        # also passed, 28ms, 写起来比加的更复杂，考虑的边界条件要更多
        n = len(nums)
        if n== 0:   
            return 0
        if n == 1 or n == 2:
            return max(nums)
        
        dp = [0] * n   
        dp[0], dp[1] = nums[0], max(nums[:2])
        for i in range(2, n):
            dp[i] = max(nums[i]+dp[i-2], dp[i-1])
        return dp[n-1]   # or return max(dp)
          

def main():
    q = Q198()
    q.add_case(q.case([1, 2, 3, 1]))
    q.run()


if __name__ == '__main__':
    main()
