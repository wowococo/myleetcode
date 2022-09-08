from leezy import solution, Solution


class Q496(Solution):
    @solution
    def nextGreaterElement(self, nums1, nums2):
        # 暴力法当然可以，遍历 nums1, 对每个元素num找到其在 nums2 中的位置，
        # 然后往后依次查找第一个大于 num的元素， 遍历到结尾，找不到的话就是-1, 时间复杂度是 o(n²)
        # 遇到下一个最大的元素，首先就要想到单调栈
        stack = []
        memo = {}
        m, n = len(nums1), len(nums2)
        for i in range(n-1, -1, -1):
            v = nums2[i]
            while stack and stack[-1] < v:
                stack.pop()
            if stack:
                memo[v] = stack[-1]
            else:
                memo[v] = -1
            stack.append(v)
        
        ans = []
        for i in range(m):
            ans.append(memo.get(nums1[i]))

        return ans

def main():
    q = Q496()
    q.add_case(q.case([4, 1, 2], [1, 3, 4, 2]))
    q.run()


if __name__ == '__main__':
    main()
