from leezy import solution, Solution
from random import randint

class Q912(Solution):
    @solution
    def sortArray(self, nums):
        # 使用快速排序 O(nlogn)  O(1),这种方法不适用于求最大K,最小K，它的分界是一条线，这条线左边的都比它小，右边的都比它大
        def quick_sort(l, r):
            if l >= r: return
            i, j = l, r
            m = l + randint(0, r - l)  # 确定分界点下标
            pivot = nums[m]
            while i <= j:
                while nums[i] < pivot: i += 1
                while nums[j] > pivot: j -= 1
                if i <= j:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                    j -= 1
            quick_sort(l, j)
            quick_sort(i, r)
            
        quick_sort(0, len(nums)-1)
        return nums

    @solution
    def sortArray_common(self, nums):
        # 快排 适用于求最大K，最小K，分界点是一个具体的数值，这个分界点左边的都比这个数小，右边的都比这个数大
        def quick_sort(lo, hi):
            if lo >= hi:
                return
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

            quick_sort(lo, j-1)
            quick_sort(j+1, hi)
        
        quick_sort(0, len(nums)-1)
        return nums

def main():
    q = Q912()
    q.add_case(q.case([5, 2, 3, 1]).assert_equal([1, 2, 3, 5]))
    q.add_case(q.case([5,1,1,2,0,0]).assert_equal([0, 0, 1, 1, 2, 5]))
    q.add_case(q.case([6, 1, 2, 7, 9]).assert_equal([1, 2, 6, 7, 9]))
    q.run()


if __name__ == '__main__':
    main()
