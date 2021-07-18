from leezy import solution, Solution


class Q031(Solution):
    @solution
    def nextPermutation(self, nums):
        # 36ms, 80.84%
        N = len(nums)
        if N <= 1:
            return
        i, j, k = N - 2, N - 1, N - 1
        while i >= 0 and nums[i] >= nums[j]:
            i -= 1
            j -= 1
        if i >= 0:
            while nums[i] >= nums[k]:
                k -= 1
            nums[i], nums[k] = nums[k], nums[i]
        
        i, j = j, N-1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        # return nums

def main():
    q = Q031()
    q.add_case(q.case([1, 2, 3]))
    q.add_case(q.case([1,2,3,5,4,3]))
    q.add_case(q.case([3, 2, 1]))
    q.run()


if __name__ == '__main__':
    main()
