from leezy import solution, Solution


class Q198(Solution):
    @solution
    def rob(self, nums):
        pre_max = 0
        current_max = 0
        for num in nums:
            temp = current_max
            # f(k) = 从前 k 个房屋中能抢劫到的最大数额,k为第k个房屋的钱数
            # f(k) = max(f(k-2)+k, f(k-1))
            current_max = max(pre_max+num, current_max)
            pre_max = temp
        return current_max
            


def main():
    q = Q198()
    q.add_case(q.case([1, 2, 3, 1]).assert_equal(4))
    q.add_case(q.case([2,1,1,2]).assert_equal(4))
    q.run()

if __name__ == '__main__':
    main()
