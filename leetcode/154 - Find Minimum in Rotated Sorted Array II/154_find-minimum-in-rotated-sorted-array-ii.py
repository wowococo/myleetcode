from leezy import solution, Solution


class Q154(Solution):
    @solution
    def findMin(self, nums):
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] < nums[r]:   # con1
                r = mid
            elif nums[mid] == nums[r]:
                r -= 1
            else:
                l = mid + 1

        return nums[l]

# the reason why the '=' is not here is there are duplicate elements in the array.
# for example:
# 1 2 3 3 3 3 3 - >  3 3 3 3 1 2 3
def main():
    q = Q154()
    q.add_case(q.case([1, 3, 5]).assert_equal(1))
    q.add_case(q.case([2, 2, 2, 0, 1]).assert_equal(0))
    q.add_case(q.case([3,3,1,3]).assert_equal(1))
    q.add_case(q.case([3,1,3]).assert_equal(1))
    q.run()
 

if __name__ == '__main__':
    main()
