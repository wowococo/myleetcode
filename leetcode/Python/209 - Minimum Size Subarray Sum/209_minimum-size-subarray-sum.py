from leezy import solution, Solution


class Q209(Solution):
    @solution
    def minSubArrayLen(self, target, nums):
        # 前缀和
        n = len(nums)
        # prefixsums 的长度必须是 n+1,给求全数组的前缀和预留一个-1 位置，而避免被 python -1 索引干扰
        prefixsums = [0] * (n+1)
        for i in range(1, n+1):
            prefixsums[i] = prefixsums[i-1] + nums[i-1]

        def found(span: int) -> bool:
            for i in range(n, 0, -1):
                if prefixsums[i] - prefixsums[i-span] >= target:
                    return True
            return False

        l, r = 1, n + 1
        while l < r:
            mid = l + (r - l) // 2
            if found(mid):
                r = mid
            else:
                l = mid + 1
        return l if sum(nums) >= target else 0


def main():
    q = Q209()
    # q.add_case(q.case(7, [2, 3, 1, 2, 4, 3]).assert_equal(2))
    q.add_case(q.case(15, [1,2,3,4,5]).assert_equal(5))
    q.run()


if __name__ == '__main__':
    main()

