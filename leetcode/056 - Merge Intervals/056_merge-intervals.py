from leezy import solution, Solution


class Q056(Solution):
    @solution
    def merge(self, intervals):
        # 36ms 90.02%
        intervals = sorted(intervals)
        N = len(intervals)
        ans = [intervals[0]]
        for i in range(1, N):
            if intervals[i][0] > ans[-1][1]:
                ans.append(intervals[i])
            else:
                ans[-1] = [ans[-1][0], max(intervals[i][1], ans[-1][1])]
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
