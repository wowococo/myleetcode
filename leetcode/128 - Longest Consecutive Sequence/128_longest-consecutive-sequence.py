from leezy import solution, Solution


class Q128(Solution):
    @solution
    def longestConsecutive(self, nums):
        # hashtable {key: len} 以这个 key为边界的最长连续序列的长度
        # 108ms 31.34%
        h = {}
        ans = 0
        for num in nums:
            if num in h:
                continue
            length = 1
            if num - 1 in h:
                # num should be put in the right side
                length += h[num-1]
            if num + 1 in h:
                length += h[num+1]
            if num - 1 in h:
                h[num-h[num-1]] = length
            if num + 1 in h:
                h[num + h[num+1]] = length

            h[num] = length
            ans = max(ans, length)

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
