from leezy import solution, Solution


class Q704(Solution):
    @solution
    def search(self, nums, target):
        l, h = 0, len(nums)
        while l < h:
            m = l + (h - l) // 2
            if nums[m] == target:
                return m
            if nums[m] > target:
                h = m
            else:
                l = m + 1
        return -1

def main():
    q = Q704()
    q.add_case(q.case([-1, 0, 3, 5, 9, 12], 9))
    q.run()


if __name__ == '__main__':
    main()
