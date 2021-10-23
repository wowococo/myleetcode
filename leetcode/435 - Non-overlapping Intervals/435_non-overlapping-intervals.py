from leezy import solution, Solution


class Q435(Solution):
    @solution
    def eraseOverlapIntervals(self, intervals):
        # 移除掉最小数量的区间使得剩余的区间不重叠，等于找到数量最多的不重叠区间
        # 贪心算法就是：每一步都走局部最优解，最后就是全局最优解。
        # 1. 定义 x，x 是当前所有区间中 end 最小的
        # 2. 遍历区间，遇到与 x 相交的区间都删掉，当然也包括 x 自身
        # 3. 重复 1和 2，直到 intervals 为空，先前选出的所有 x 就是最多不相交区间
        if len(intervals) == 0:
            return 0
        intervals = sorted(intervals, key=lambda x: x[1])
        end = intervals[0][1]
        count = 1
        for intv in intervals:
            start = intv[0]
            if start >= end:
                end = intv[1]
                count += 1
                
        return len(intervals) - count



def main():
    q = Q435()
    q.add_case(q.case([[1, 2], [2, 3], [3, 4], [1, 3]]).assert_equal(1))
    q.run()


if __name__ == '__main__':
    main()
