from leezy import solution, Solution


class Q034(Solution):
    @solution
    def searchRange(self, nums, target):
        l, r = 0, len(nums)
        while l < r:
            m = l + (r - l) // 2
            if nums[m] >= target:
                r = m
            else:
                l = m + 1
        start = l
        print(start)
        l, r = 0, len(nums)
        while l < r:
            m = l + (r - l) // 2
            if nums[m] > target:
                r = m
            else:
                l = m + 1
        if start == len(nums) or nums[start] != target:
            return [-1, -1]
        return [start, l-1]
def main():
    q = Q034()
    q.add_case(q.case([5, 7, 7, 8, 8, 10], 8).assert_equal([3, 4]))
    q.add_case(q.case([5, 7, 7, 8, 8, 10], 6).assert_equal([-1, -1]))
    q.add_case(q.case([1], 1).assert_equal([0, 0]))
    q.add_case(q.case([2, 2], 2).assert_equal([0,1]))
    q.add_case(q.case([1,2], 2).assert_equal([1,1]))
    q.run()


if __name__ == '__main__':
    main()
