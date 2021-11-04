from leezy import solution, Solution


class Q453(Solution):
    @solution
    def minMoves(self, nums):
        # 算是一道脑筋急转弯, 给 n-1 个元素+1 相当于给 1 个元素 -1
        # 时间复杂度：o(n)，空间复杂度: o(1) 52ms 39.1%
        min_num = min(nums)  #o(n)
        res = 0
        for num in nums: # o(n)
            res += num - min_num
        return res


def main():
    q = Q453()
    q.add_case(q.case([1, 2, 3]))
    q.run()


if __name__ == '__main__':
    main()
