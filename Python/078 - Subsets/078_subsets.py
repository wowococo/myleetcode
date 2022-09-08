from leezy import solution, Solution


class Q078(Solution):
    @solution
    def subsets(self, nums):
        # 32ms 77.93%
        N = len(nums)
        cur, total = [], []

        def dfs(n, s):
            if len(cur) == n:
                total.append(cur[:])
                return
            for i in range(s, N):
                cur.append(nums[i])
                dfs(n, i+1)
                cur.pop()

        for i in range(N+1):
            dfs(i, 0)

        return total


def main():
    q = Q078()
    q.add_case(q.case([1, 2, 3]).assert_equal([[], [1], [2], [3], [1, 2],[1, 3], [2, 3], [1, 2, 3]] ))
    q.add_case(q.case([1]).assert_equal( [[], [1]]))
    q.run()


if __name__ == '__main__':
    main()
