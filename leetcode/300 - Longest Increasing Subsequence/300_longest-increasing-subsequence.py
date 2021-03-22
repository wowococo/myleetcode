from leezy import solution, Solution


class Q300(Solution):
    @solution
    def lengthOfLIS(self, nums):
        # o(nlogn)
        # dp[i] 表示长度为 i+1 的最长递增子序列的最小 ending number
        from bisect import bisect_left
        dp = []
        for x in nums:
            i = bisect_left(dp, x)
            if i == len(dp):
                dp.append(x)
            else:
                dp[i] = x
        return len(dp)

    @solution
    def lengthOfLIS(self, nums):
        # o(n^2)
        # dp[i] 表示以 nums[i] 为结尾的最长递增子序列的长度,这题是一维dp,二维时间复杂度
        n = len(nums)
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)

   

def main():
    q = Q300()
    q.add_case(q.case([10, 9, 2, 5, 3, 7, 101, 18]).assert_equal(4))
    q.run()


if __name__ == '__main__':
    main()
