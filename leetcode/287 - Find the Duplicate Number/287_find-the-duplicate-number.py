from leezy import solution, Solution


class Q287(Solution):
    @solution
    def findDuplicate(self, nums):
        # 转化为找环形链表的环入口点 96ms 75.99%
        fast = slow = 0
        slow = nums[slow]
        fast = nums[nums[fast]]
        while fast != slow:
            slow = nums[slow]
            fast = nums[nums[fast]]
        
        cursor = 0
        while cursor != slow:
            cursor = nums[cursor]
            slow = nums[slow]
        
        return cursor

def main():
    q = Q287()
    q.add_case(q.case([1, 3, 4, 2, 2]).assert_equal(2))
    q.add_case(q.case([1,1]).assert_equal(1))
    q.add_case(q.case([3,1,2,3,4]).assert_equal(3))
    q.run()


if __name__ == '__main__':
    main()
