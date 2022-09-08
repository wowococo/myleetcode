from leezy import solution, Solution


class Q035(Solution):
    @solution
    def searchInsert(self, nums, target):
        # binary search
        l = 0
        r = len(nums)
        while l < r:
            m = l + (r - l) // 2
            if nums[m] == target:
                return m
            if nums[m] > target:
                r = m
            else:
                l = m + 1
        return l

def main():
    q = Q035()
    q.add_case(q.case([1, 3, 5, 6], 5).assert_equal(2))
    q.add_case(q.case([1, 3, 5, 6], 7).assert_equal(4))
    q.add_case(q.case([1, 3, 5, 6], 0).assert_equal(0))
    q.add_case(q.case([1, 3, 5, 6], 2).assert_equal(1))
    q.run()


if __name__ == '__main__':
    main()
