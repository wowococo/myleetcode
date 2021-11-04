from leezy import solution, Solution


class Q056(Solution):
    @solution
    def merge(self, intervals):
        # 36ms 90.02%
        intervals = sorted(intervals)
        N = len(intervals)
        if N < 1:
            return []
        ans = [intervals[0]]
        for itl in intervals[1:]:
            if ans[-1][1] >= itl[0]:
                ans[-1] = [ans[-1][0], max(ans[-1][1], itl[1])]
            else:
                ans.append(itl)
        return ans
            
def main():
    q = Q056()
    q.add_case(q.case([[1, 3], [2, 6], [8, 10], [15, 18]]))
    q.add_case(q.case([[1,4],[4,5]]))
    q.add_case(q.case([[1,4],[4,5], [5,6]]))
    q.add_case(q.case([[1,4],[2,3]]).assert_equal([[1,4]]))
    q.run()


if __name__ == '__main__':
    main()
