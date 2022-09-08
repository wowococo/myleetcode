from leezy import solution, Solution


class Q152(Solution):
    @solution
    def maxProduct(self, nums):
        # 维护一个max和一个min，因为有负数，负数*负数为正数，上次最小的乘以当前值可能就是此次最小的
        if not nums: return 0
        roll_max = nums[0]
        roll_min = nums[0]
        ans = nums[0]
        for x in nums[1:]:
            cands = (x * roll_max, x * roll_min, x)
            roll_max = max(cands)
            roll_min = min(cands)
            ans = max(ans, roll_max)
        return ans


def main():
    q = Q152()
    q.add_case(q.case([2, 3, -2, 4]).assert_equal(6))
    q.add_case(q.case([-2,0,-1]).assert_equal(0))
    q.add_case(q.case([0.1, 0.0, 3.0, -2.0, 0.9, -1.3, 5.0, -4.4]).assert_equal(35.1))
    q.run()


if __name__ == '__main__':
    main()
