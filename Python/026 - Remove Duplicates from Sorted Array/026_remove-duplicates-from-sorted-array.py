from leezy import solution, Solution


class Q026(Solution):
    @solution
    def removeDuplicates(self, nums):
        # 删除有序数组中重复的元素，首先要想到双指针之快慢指针
        slow = fast = 0
        while fast < len(nums):
            # 因为数组是有序的，所以可以这样比较
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
            
            fast += 1
        
        return slow + 1


def main():
    q = Q026()
    q.add_case(q.case([1, 1, 2]))
    q.run()


if __name__ == '__main__':
    main()
