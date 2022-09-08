from leezy import solution, Solution


class Q283(Solution):
    @solution
    def moveZeroes(self, nums):
        # 28ms 98.65%
        j = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[j] = nums[i]
                j += 1
        for i in range(j, len(nums)):
            nums[i] = 0
        return nums

    @solution
    def moveZeroesQS(self, nums):
        # 以快排的思路，以 0 为分界点，它的左边放不为 0 的数，右边放等于 0 的数。
        j = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
        return nums


def main():
    q = Q283()
    q.add_case(q.case([0, 1, 0, 3, 12]).assert_equal([1, 3, 12, 0, 0]))
    q.add_case(q.case([0, 0, 1]).assert_equal([1, 0, 0]))
    q.run()


if __name__ == '__main__':
    main()
