from leezy import solution, Solution


class Q033(Solution):
    @solution
    def search(self, nums, target):
        # O(n)
        for i in range(len(nums)-1):
            if nums[i] == target:
                return i
        return -1
    
    @solution
    def search_binary(self, nums, target):
        if len(nums) == 0:
            return -1
        # O(log n)
        l = 0
        r = len(nums) - 1
        while l < r:   # 当 l == r 时,跳出循环
            mid = l + (r - l) // 2
            if nums[mid] < nums[r]:  # [mid, r] 有序
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid
            else:  # [l, mid]有序
                if nums[l] <= target <= nums[mid]:
                    r = mid
                else:
                    l = mid + 1
        return r if nums[r] == target else -1
        # return l if nums[l] == target else -1


        

def main():
    q = Q033()
    q.add_case(q.case([4, 5, 6, 7, 0, 1, 2], 0).assert_equal(4))
                    #  0, 1, 2, 3, 4, 5, 6
    q.add_case(q.case([4, 5, 6, 7, 0, 1, 2], 3).assert_equal(-1))
    q.add_case(q.case([1], 1).assert_equal(0))
    q.run()


if __name__ == '__main__':
    main()
