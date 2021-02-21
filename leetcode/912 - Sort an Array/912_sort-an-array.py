from leezy import solution, Solution
from random import randint

class Q912(Solution):
    @solution
    def sortArray(self, nums):
        # 使用快速排序 O(nlogn)  O(1)
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


def main():
    q = Q912()
    q.add_case(q.case([5, 2, 3, 1]))
    q.run()


if __name__ == '__main__':
    main()
