from leezy import solution, Solution


class Q153(Solution):
    @solution
    def findMin(self, nums):
        l , r = 0, len(nums) - 1
        while  l < r:
            mid = l + (r - l) // 2
            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1
        return nums[l]


def main():
    q = Q153()
    q.add_case(q.case([3, 4, 5, 1, 2]).assert_equal(1))
    q.add_case(q.case([4, 5, 6, 7, 1, 2, 3]).assert_equal(1))
    q.add_case(q.case([4, 5, 6, 7, 0, 1, 2]).assert_equal(0))
    q.run()


if __name__ == '__main__':
    main()
