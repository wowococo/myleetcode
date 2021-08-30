from leezy import solution, Solution


class Q128(Solution):
    @solution
    def longestConsecutive(self, nums):
        # 要求 O(n), 强烈提示使用哈希表,如果排序的话，复杂度是 O(nlogn)
        stat = {}
        ans = 0
        for num in nums:
            if num in stat:
                continue
            length = 1  
            if num + 1 in stat:
                # num should be put at the left side
                length += stat[num+1]
            if num - 1 in stat:
                # num should be put at the right side
                length += stat[num-1]

            stat[num] = length

            if num + 1 in stat:
                stat[num + stat[num+1]] = length
            if num - 1 in stat:
                stat[num - stat[num-1]] = length

            ans = max(ans, length)

        return ans

            



def main():
    q = Q128()
    q.add_case(q.case([100, 4, 200, 1, 3, 2]))
    q.run()


if __name__ == '__main__':
    main()
