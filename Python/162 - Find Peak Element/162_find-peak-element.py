from leezy import solution, Solution


class Q162(Solution):
    @solution
    def findPeakElement(self, nums):
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] > nums[mid + 1]:
                r = mid
            else:
                l = mid + 1
        return l


def main():
    q = Q162()
    q.add_case(q.case([1, 2, 3, 1]).assert_equal(2))
    q.add_case(q.case([1,2,1,3,5,6,4]).assert_equal(5))
    q.run()


if __name__ == '__main__':
    main()
