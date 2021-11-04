from leezy import solution, Solution


class Q053(Solution):
    @solution
    def maxSubArray(self, nums):
        # kadane's algorithm
        sum = max_sum = nums[0]
        for i in range(1, len(nums)):
            sum = max(sum+nums[i], nums[i])
            max_sum = max(max_sum, sum)
        return max_sum

    @solution
    def maxSubArray_dp(self, nums):
        dp = [0] * len(nums)
        for i in range(len(nums)):
            dp[i] = max(dp[i-1]+nums[i], nums[i])
        return max(dp)

    @solution
    def maxSubArray_dp2(self, nums):
        n, i = len(nums), 1
        dp = [0] * n    
        dp[0] = nums[0]
        maxsub = dp[0]
        while i < n:
            dp[i] = nums[i] + (dp[i - 1] if dp[i - 1] > 0 else 0)
            maxsub = max(dp[i], maxsub)
            i += 1
        return maxsub



def main():
    q = Q053()
    q.add_case(q.case([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    q.run()


if __name__ == '__main__':
    main()
