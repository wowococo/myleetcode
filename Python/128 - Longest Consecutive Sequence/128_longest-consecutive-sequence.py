from leezy import solution, Solution


class Q128(Solution):
    @solution
    def longestConsecutive(self, nums):
        # 如果使用排序的话，复杂度一般要 O(nlogn)
        # 要求 O(n), 强烈提示使用哈希表, hashtable {key: len} 以这个 key为边界的最长连续序列的长度
        # 108ms 31.34%
        h = {}
        ans = 0
        for num in nums:
            if num in h:
                continue
            length = 1
            if num - 1 in h:
                # num should be put at the right side
                length += h[num-1]
            if num + 1 in h:
                # num should be put at the left side
                length += h[num+1]
            if num - 1 in h:
                h[num-h[num-1]] = length
            if num + 1 in h:
                h[num + h[num+1]] = length

            h[num] = length
            ans = max(ans, length)

        return ans

    @solution
    def longest_consecutive(self, nums):
        # 1732ms 12.25%  
        h = {}
        for num in nums:
            h[num] = num
        ans = 0
        for num in nums:
            if num-1 not in h: # o(1)
                l = 0
                while num in h: # o(2) 每个只会被访问两次
                    l += 1
                    num += 1
                ans = max(ans, l)
        
        return ans
        



def main():
    q = Q128()
    q.add_case(q.case([100, 4, 200, 1, 3, 2]).assert_equal(4))
    q.add_case(q.case([1, 100]).assert_equal(1))
    q.add_case(q.case([0,1,2,3,4,5,6]).assert_equal(7))
    q.add_case(q.case([1,2,0,1]).assert_equal(3))
    q.run()


if __name__ == '__main__':
    main()
