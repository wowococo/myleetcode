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
