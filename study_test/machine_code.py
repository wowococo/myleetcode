from leezy.assists import LinkedListContext, ListNode
from leezy import solution, Solution
import re
s = "(2 * (3-4)) * 5"

def solve(nums):
    dp = [1] * (len(nums) + 1)
    for i in range(1, len(nums)+1):
        dp[i] = 0
        if nums[i-1] != '0':
            dp[i] = dp[i-1]
        if i > 1 and nums[i-2] != '0' and int(nums[i-2:i]) <= 26:
            dp[i] += dp[i-2]
        if dp[i] == 0:
            return 0
    return dp[-1]

def translateNum(num: int) -> int:
    nums = str(num)
    n = len(nums)
    dp = [1] * (n+1)
    for i in range(1, n+1):
        dp[i] = dp[i-1]
        if i > 1 and nums[i-2] != '0' and int(nums[i-2:i]) < 26:
            dp[i] += dp[i-2]
    return dp[-1]

def isMatch(self , s , pattern):
    memo = [[None] * (len(pattern)+1) for _ in range(len(s)+1)]
    def imatch(i, j):
        if j == len(pattern):
            return i == len(s)
        if memo[i][j] is not None:
            return memo[i][j]
        ans = None
        has_s = i < len(s)
        if pattern[j] == '?':
            ans = imatch(i+1, j+1) if has_s else False
        elif pattern[j] == '*':
            ans = imatch(i, j+1)
            if has_s:
                ans = ans or imatch(i+1, j+1) or imatch(i+1, j)
        else:
            ans = has_s and pattern[j] == s[i] and imatch(i+1, j+1)
        memo[i][j] = ans
        return ans
    return imatch(0, 0)

class A:
    def subsequence(self, n , array ):
        # write code here
        cur = []
        total = []
        self.max_sum = 0
        def dfs(l, s):
            if len(cur) == l:
                print(cur)
                total.append(cur.copy())
                self.max_sum = max(self.max_sum, sum(cur))
                return
            for i in range(s, n):
                cur.append(array[i])
                dfs(l, i+2)
                cur.pop()
        print(n)
        for i in range(n+1):
            dfs(i, 0)

        return self.max_sum

def solve(matrix):
    m, n = len(matrix), len(matrix[0])
    grid = [[0] * (n+1) for _ in range(m+1)]
    ans = 0 
    for i in range(1, m+1):
        for j in range(1, n+1):
            if matrix[i-1][j-1] == '1':
                grid[i][j] = 1 + min(
                    grid[i-1][j],
                    grid[i-1][j-1],
                    grid[i][j-1]
                )
                ans = max(ans, grid[i][j])
    return ans * ans


def reorderList(self , head ):
    if not head or not head.next or not head.next.next:
        return head
    slow = head
    fast = head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    node = slow.next
    slow.next = None
    while node:
        nxt = node.next
        node.next = slow.next
        slow.next = node
        node = nxt

    r = slow.next
    slow.next = None
    l = head
    while r:
        nxt_r = r.next
        nxt_l = l.next
        r.next = l.next
        l.next = r
        l = nxt_l
        r = nxt_r
    return head


def thenumberof0(self , n ):
    ans = 0
    div = 5
    while div <= n:
        ans += n // div 
        div *= 5
    return ans


def NumberOf1(self, n):
    ans = 0
    mask = 0xFFFFFFFF
    while n:
        ans += 1
        n = n & (n-1) & mask
    return ans

def permute(num):
    # write code here
    cur, total =[], []
    m = len(num)
    used = [False] * m
    def dfs(n):
        if len(cur) == n:
            print(cur)
            total.append(cur.copy())
            return
        for i in range(m):
            if used[i]:
                continue
            used[i] = True
            cur.append(num[i])
            dfs(n)
            cur.pop()
            used[i] = False 
    dfs(m)
    return total

def permuteUnique( num ):
    # write code here
    cur, total = [], []
    used = [False] * len(num)
    def dfs(n):
        if len(cur) == n:
            total.append(cur[:])
            return
        prev = None
        for i in range(len(num)):
            if used[i] or num[i] == prev:
                continue 
            used[i] = True
            prev = num[i]
            cur.append(num[i])
            dfs(n)
            cur.pop()
            used[i] = False
    dfs(len(num))
    return total

def maxPathSum(self , root ):
    MIN = float('-inf')
    self.ans = MIN
    def walk(node):
        if node is None:
            return MIN
        left = walk(node.left)
        right = walk(node.right)
        solo_included_max = max(
            node.val,
            left + node.val,
            right + node.val,
        )
        self.ans = max(self.ans, solo_included_max, left + right + node.val)
        return solo_included_max
    walk(root)
    return self.ans


class Q(Solution):
    def reverseBetween(self, head , m , n ):
        # write code here
        dummy = ListNode(0)
        dummy.next = head
        count = 0
        
        while head:
            count += 1
            if count == m - 1:
                front = head
                print(front.val)
            if count == m:
                cur = head
                print(cur.val)
            if count == n + 1:
                behind = head
                print(behind.val)
            head = head.next
        if m == 1:
            front = dummy
            print(front.val)
        if count == n:
            behind = None
        prev = behind
        while cur != behind:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        front.next = prev
        
        return dummy.next
            
def reverseKGroup(self , head , k ):
    if not head:
        return
    glb_head = ListNode(None)
    grp_dummy = glb_head
    grp_tail = head
    cnt = 0
    node = head
    while node:
        if cnt > 0 and cnt % k == 0:
            grp_dummy = grp_tail
            grp_dummy.next = None
            grp_tail = node
        nxt = node.next
        node.next = grp_dummy.next
        grp_dummy.next = node
        node = nxt
        cnt += 1

    if cnt % k != 0:
        node = grp_dummy.next
        grp_dummy.next = None
        while node:
            nxt = node.next
            node.next = grp_dummy.next
            grp_dummy.next = node
            node = nxt
    return glb_head.next

    
if __name__ == '__main__':
    q = Q()
    
    l = ListNode.make_linked_list([1, 2, 3, 4, 5])
    print(q.reverseBetween(l, 2,4))




def maxlenEqualK(arr , k ):  
    memo = {0: 0}
    prefix_sum = 0  
    ans = 0
    for i, n in enumerate(arr, 1):
        prefix_sum += n
        if prefix_sum not in memo:
            memo[prefix_sum] = i
        counterpart = prefix_sum - k
        if counterpart in memo:
            ans = max(i - memo[counterpart], ans)
    return ans

def longestValidParentheses(self , s ):
    # write code here
    farest = -1
    ans = 0
    stack = []
    for i, ch in enumerate(s):
        if ch == '(':
            stack.append(i)
        else:
            if stack:
                stack.pop()
                ans = max(ans, i-(stack[-1] if stack else farest))
            else:
                farest = i
    return ans

def logged(func):
    def with_logging(*args, **kwargs):
        print(func.__name__ + " was called")
        return func(*args, **kwargs)
    return with_logging

def f(x):
    """does some math"""
    return x + x * x

if __name__ == "__main__":
    f = logged(f)
