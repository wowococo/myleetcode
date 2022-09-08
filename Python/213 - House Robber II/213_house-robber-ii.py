from leezy import solution, Solution


class Q213(Solution):
    @solution
    def rob(self, nums):
        if len(nums) == 1:
            return nums[0]
        pre_max1, pre_max2 = [0,0]
        current_max1, current_max2 = [0,0]
        nums1 = nums[:-1]
        nums2 = nums[1:]
        for num in nums1:
            temp = current_max1
            current_max1 = max(pre_max1+num, current_max1)
            pre_max1 = temp

        for num in nums2:
            temp = current_max2
            current_max2 = max(pre_max2+num, current_max2)
            pre_max2 = temp
        return max(current_max1, current_max2)

    @solution
    def rob_dp(self, nums):
        # 28ms 88.23%
        # 首尾不能同时抢，可分为三种情况，首尾都不抢、首抢尾不抢、首不抢尾抢
        n = len(nums)
        # don't forget
        if n == 1:
            return nums[0]
        dp1 = dp2 = [0] * (n+2)
        # 首抢尾不抢
        for i in range(n-2, -1, -1):
            dp1[i] = max(nums[i]+dp1[i+2], dp1[i+1])
        # 首不抢尾抢
        for i in range(n-1, 0, -1):
            dp2[i] = max(nums[i]+dp2[i+2], dp2[i+1])
        
        return max(dp1[0], dp2[1])

    @solution
    def rob_less_space(self, nums):
        # 可以将一维 dp 降为几个变量 24ms, 96.79%
        n = len(nums)
        if n == 1:
            return nums[0]
        return max(self.rob_range(0, n-2, nums), self.rob_range(1, n-1, nums))
    
    # [start, end] 为闭区间
    def rob_range(self, start, end, nums):
        dp_i_1, dp_i_2 = 0, 0
        dp_i = 0
        for i in range(end, start-1, -1):
            dp_i = max(nums[i]+dp_i_2, dp_i_1)
            dp_i_2, dp_i_1 = dp_i_1, dp_i
        return dp_i


def main():
    q = Q213()
    q.add_case(q.case([2, 3, 2]).assert_equal(3))
    q.add_case(q.case([1,2,3,1]).assert_equal(4))
    q.add_case(q.case([1,2,1,1]).assert_equal(3))
    q.add_case(q.case([1,2]).assert_equal(2))
    q.add_case(q.case([1]).assert_equal(1))
    q.run()

if __name__ == '__main__':
    main()
