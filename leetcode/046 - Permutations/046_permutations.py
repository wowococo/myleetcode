from leezy import solution, Solution


class Q046(Solution):
    @solution
    def permute(self, nums):
        # 32ms 95.48%
        cur, total = [], []
        N = len(nums)
        used = [False] * N
        def dfs():
            if len(cur) ==  N:
                total.append(cur[:])
                return
            for i in range(N):
                if used[i]:
                    continue
                used[i] = True
                cur.append(nums[i])
                dfs()
                cur.pop()
                used[i] = False

        dfs()
        return total

def main():
    q = Q046()
    q.add_case(q.case([1, 2, 3]))
    q.run()


if __name__ == '__main__':
    main()
