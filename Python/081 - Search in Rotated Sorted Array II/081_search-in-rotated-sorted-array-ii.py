from leezy import solution, Solution


class Q081(Solution):
    @solution
    def search(self, nums, target):
        if len(nums) == 1 and nums[0] == target:
            return True
        else:
            return False
        l, r = 0, len(nums)-1
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] < nums[r]:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid
            else:
                if nums[l] <= target <= nums[mid]:
                    r = mid
                else:
                    l = mid + 1
        return True if nums[l] == target else False

# 01222222222222222232234
# 223401222222222222222223
    

def main():
    q = Q081()
    q.add_case(q.case([2, 5, 6, 0, 0, 1, 2], 0))
    q.add_case(q.case([2, 5, 6, 0, 0, 1, 2], 3))
    q.run()


if __name__ == '__main__':
    main()
