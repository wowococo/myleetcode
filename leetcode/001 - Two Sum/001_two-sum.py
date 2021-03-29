from leezy import solution, Solution


class Q001(Solution):
    @solution
    def twoSum(self, nums, target):
        # 此题要求返回的是下标，因为不能直接对原数组按照数大小进行排序，因为这样会改变数的位置，
        # 因此有个很巧妙的思路是： 对数组的索引按照每个索引在数组中对应的值的大小，对索引进行排序（默认就是升序）
        if nums is None or len(nums) < 2:
            return []
        n = len(nums)
        indexs = sorted(range(n), key=lambda i: nums[i])
        # i，j代表 indexs 的索引  
        i, j = 0, len(indexs) - 1     # 或者 i, j = 0, len(nums) - 1
        
        while i < j:
            s = nums[indexs[i]] + nums[indexs[j]]
            if s < target:
                i += 1
            elif s > target:
                j -= 1
            else:
                return sorted([indexs[i], indexs[j]])


def main():
    q = Q001()
    q.add_case(q.case([2, 7, 11, 15], 9).assert_equal([0, 1]))
    q.add_case(q.case([3, 2, 4], 6).assert_equal([1, 2]))
    q.run()

if __name__ == '__main__':
    main()
