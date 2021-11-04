from leezy import solution, Solution


class Q238(Solution):
    @solution
    def productExceptSelf(self, nums):
        # 这个数左边的乘积 * 这个数右边的乘积 
        # 84ms 23.82%
        n = len(nums)
        k = 1
        res = [1] * n
        # 左边数的乘积
        for i in range(1, n):
            res[i] = res[i-1] * nums[i-1]
        # 所有数的乘积
        k = 1
        for i in range(n-2, -1, -1):
            k *= nums[i+1]
            res[i] *= k
        
        return res


def main():
    q = Q238()
    q.add_case(q.case([1, 2, 3, 4]))
    q.run()


if __name__ == '__main__':
    main()
