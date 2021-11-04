from leezy import solution, Solution


class Q435(Solution):
    # @solution
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


class Qalixin_3(Solution):
    # @solution
    def minSubstringCount(self, s):
        # 字符串由小写字母构成，将一个字符串拆分为几个子字符串，要求每个子字符串不能有重复的字符，求最少的满足条件的子字符串个数。
        # 如果用贪心算法的话，每一个局部最优来完成全局最优，那么局部最优是什么？局部最优就是字符前缀在不重复的情况下尽可能的长。
        # 如何判断字符是否有重复的？判断其 ord(ch) 序号是否相等。
        count = 0
        memo = []
        for ch in s:
            if ch in memo:
                count += 1
                memo = [ch]
            else:
                memo.append(ch)
        
        return count + 1

    @solution
    def t3(self, s):
        ans = 1
        memo = [0] * 26
        base = ord('a')
        for ch in s:
            idx = ord(ch) - base
            if memo[idx] == ans:
                ans += 1
            memo[idx] = ans
        
        return ans


def main():
    q = Q435()
    q.add_case(q.case([[1, 2], [2, 3], [3, 4], [1, 3]]).assert_equal(1))
    q.run()

    qalixin = Qalixin_3()
    qalixin.add_case(qalixin.case('cycle').assert_equal(2))
    qalixin.add_case(qalixin.case('world').assert_equal(1))
    qalixin.add_case(qalixin.case('dddd').assert_equal(4))
    qalixin.add_case(qalixin.case('setting').assert_equal(2))
    qalixin.add_case(qalixin.case('alibaba').assert_equal(3))
    qalixin.run()


if __name__ == '__main__':
    main()
