from leezy import solution, Solution


class Q055(Solution):
    @solution
    def canJump(self, nums):
        # 88ms 65.15%
        n = len(nums)
        # k 表示可以跳到的最大位置的下标, 如果一个位置是可达的，那么它左侧的所有位置都是可达的
        k = 0
        for i in range(n):
            if i > k:
                return False
            k = max(k, i+nums[i])

        return True




def main():
    q = Q055()
    q.add_case(q.case([2, 3, 1, 1, 4]))
    q.add_case(q.case([3,2,1,0,4]))
    q.run()


if __name__ == '__main__':
    main()
