from leezy import solution, Solution


class Q448(Solution):
    @solution
    def findDisappearedNumbers(self, nums):
        # TLE
        n = len(nums)
        ans = []
        for i in range(1, n+1):
            if i not in nums:
                ans.append(i)
        return ans

    @solution
    def findDisappearedNumbersOpti(self, nums):
        # 72ms 83.86%
        n = len(nums)
        for num in nums:
            i = (num - 1) % n
            nums[i] += n
        
        res = [i+1 for i, num in enumerate(nums) if num <= n]
        return res


def main():
    q = Q448()
    q.add_case(q.case([4, 3, 2, 7, 8, 2, 3, 1]).assert_equal([5,6]))
    q.add_case(q.case([1,1]).assert_equal([2]))
    q.run()


if __name__ == '__main__':
    main()
