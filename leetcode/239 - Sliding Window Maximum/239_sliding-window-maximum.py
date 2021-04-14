from leezy import solution, Solution
from collections import deque

class Q239(Solution):
    @solution
    def maxSlidingWindow(self, nums, k):
        # monotonic queue 单调递减队列，保证队列头元素一定是当前队列的最大值，  可用 deque 实现, learn from huahua
        # 472 ms 63.38%
        q = deque()
        ans = []
        for i in range(len(nums)):
            while q and nums[q[-1]] <= nums[i]:
                q.pop()
            q.append(i)
            if i >= k - 1:
                ans.append(nums[q[0]])
            if i - k + 1 == q[0]:
                q.popleft()
        return ans


def main():
    q = Q239()
    q.add_case(q.case([1, 3, -1, -3, 5, 3, 6, 7], 3))
    q.run()


if __name__ == '__main__':
    main()
