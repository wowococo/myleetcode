from leezy import solution, Solution


class Q154(Solution):
    @solution
    def findMin(self, nums):
        if nums[0] < nums[-1]:
            return nums[0]
        # 这里就当成二分模板的一种特殊情况吧，原先的左闭右开在这里是左闭右闭，其他三个特性都一样
        l, r = 0, len(nums)-1
        while l < r:
            m = l + (r - l) // 2
            if nums[m] == nums[r]:
                r -= 1 
            elif nums[m] < nums[r]:    # 这里不要写成if 因为上面r-=1了下面又用到了r
                r = m  
            else:
                l = m + 1

        print(l)
        return nums[l]



def main():
    q = Q154()
    q.add_case(q.case([1, 3, 5]).assert_equal(1))
    q.add_case(q.case([3,4,5,1,2]).assert_equal(1))
    q.add_case(q.case([3,1]).assert_equal(1))
    q.run()


if __name__ == '__main__':
    main()


# N = len(A)
# if N == 0 or A[0] < A[-1]:
#     return A[0]
# lo, hi = 0, N - 1
# while hi - lo > 1:
#     m = (lo + hi) // 2
#     if A[m] > A[lo]:
#         lo = m
#     elif A[m] < A[lo]:
#         hi = m
#     else:
#         while lo < hi - 1 and A[m] == A[lo]:
#             lo += 1
#         if A[lo] < A[m]:
#             return A[lo]
# return A[hi]
