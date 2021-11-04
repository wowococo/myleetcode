from leezy import solution, Solution


class Q039(Solution):
    @solution
    def combinationSum(self, candidates, target):
        # 28ms 99.94%
        candidates = sorted(candidates)
        cur, total = [], []
        N = len(candidates)
        def dfs(s, target):
            if target == 0:
                total.append(cur[:])
                return
            for i in range(s, N):
                if candidates[i] > target:
                    break
                cur.append(candidates[i])
                # 常规的从 i+1开始，这个从 i 开始说明 i 本身这个数可以重复，即数字可以无限制的重复被选取
                dfs(i, target-candidates[i])
                cur.pop()
        
        dfs(0, target)

        return total

def main():
    q = Q039()
    q.add_case(q.case([2, 3, 6, 7], 7).assert_equal([[2,2,3], [7]]))
    q.add_case(q.case([2,3,5], 8).assert_equal([[2,2,2,2],[2,3,3],[3,5]]))
    q.run()


if __name__ == '__main__':
    main()
