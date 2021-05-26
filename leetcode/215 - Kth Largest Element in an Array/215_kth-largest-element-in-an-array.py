from leezy import solution, Solution


class Q215(Solution):
    @solution
    def findKthLargest(self, nums, k):
        # 从右向左求的最大，也可以将最大k转成最小K
        def quick_sort(lo, hi, k):
            # if lo >= hi:
            #     return
            pivot = nums[lo]
            i, j = lo+1, hi
            while True:
                while i <= hi and nums[i] < pivot:
                    i += 1
                while nums[j] > pivot:
                    j -= 1
                if i >= j:
                    break
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
            nums[lo], nums[j] = nums[j], nums[lo]
            big_cnt = hi - j + 1
            if big_cnt == k:
                return nums[j]
            if big_cnt > k:
                return quick_sort(j+1, hi, k)
            else:
                return quick_sort(lo, j-1, k-big_cnt)

        return quick_sort(0, len(nums)-1, k)


def main():
    q = Q215()
    q.add_case(q.case([3, 2, 1, 5, 6, 4], 2).assert_equal(5))
    q.add_case(q.case([3,2,3,1,2,4,5,5,6], 4).assert_equal(4))
    q.run()


if __name__ == '__main__':
    main()
