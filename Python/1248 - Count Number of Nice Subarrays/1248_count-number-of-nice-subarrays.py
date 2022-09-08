from leezy import solution, Solution


class Q1248(Solution):
    @solution
    def numberOfSubarrays(self, nums, k):
        prefix_cnt = [0] * (len(nums) + 1)
        sum = 0
        prefix_cnt[0] = 1
        beauty_sub_nums = 0
        for num in nums:
            sum += num & 1
            prefix_cnt[sum] += 1
            if sum >= k:
                beauty_sub_nums += prefix_cnt[sum-k]
        return beauty_sub_nums
    

def main():
    q = Q1248()
    q.add_case(q.case([1, 1, 2, 1, 1], 3))
    q.run()


if __name__ == '__main__':
    main()
