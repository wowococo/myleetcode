from leezy import solution, Solution


class Q027(Solution):
    @solution
    def removeElement(self, nums, val):
        slow = fast = 0
        while fast < len(nums):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            
            fast += 1
        
        return slow


def main():
    q = Q027()
    q.add_case(q.case([3, 2, 2, 3], 3))
    q.run()


if __name__ == '__main__':
    main()
