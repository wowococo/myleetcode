from leezy import solution, Solution
from collections import Counter

class Q740(Solution):
    @solution
    def deleteAndEarn(self, nums):
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        max_num = max(nums)
        new_nums = [0] * (max_num+1)
        num_counts = Counter(nums)
        for num in set(nums):
            new_nums[num] = num_counts[num]
        # 开始打家劫舍
        print(new_nums)
        pre_max, current_max = [0,0]
        for i in range(len(new_nums)):

            temp = current_max
            current_max = max(current_max, pre_max + i * new_nums[i])
            pre_max = temp
            print(current_max)
        return current_max


def main():
    q = Q740()
    q.add_case(q.case([3, 4, 2]).assert_equal(6))
    q.add_case(q.case([2, 2, 3, 3, 3, 4]).assert_equal(9))
    q.run()

if __name__ == '__main__':
    main()
