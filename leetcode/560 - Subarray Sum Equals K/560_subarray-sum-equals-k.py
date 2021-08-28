from leezy import solution, Solution


class Q560(Solution):
    @solution
    def subarraySum(self, nums, k):
        # TLE 61/89 O(n³)
        N = len(nums)
        count  = 0
        for i in range(N+1):
            for j in range(i):
                if sum(nums[j:i]) == k:
                    count += 1
        return count

    @solution
    def subarraySum2(self, nums, k):
        # TLE 72/89 O(n²)
        N = len(nums)
        count  = 0
        for i in range(N):
            s = 0
            for j in range(i, N): 
                s += nums[j]
                if s == k:
                    count += 1
        return count

    @solution
    def subarraySum3(self, nums, k):
        # 前缀和，第 0 项到当前项的和, O(n), O(n); python in list O(n), in dict/set O(1) 
        # 68 ms, 89.45% 
        N = len(nums)
        count  = 0
        prefix_sum = 0
        psumcnt = {0:1}

        for i in range(N):
            prefix_sum += nums[i]
        
            if psumcnt.get(prefix_sum - k):
                count += psumcnt[prefix_sum - k]
            
            if prefix_sum in psumcnt:
                psumcnt[prefix_sum] += 1
            else:
                psumcnt[prefix_sum] = 1 

        return count     
        

def main():
    q = Q560()
    q.add_case(q.case([1, 1, 1], 2).assert_equal(2))
    q.add_case(q.case([-1,-1,1], 0).assert_equal(1))
    q.run()


if __name__ == '__main__':
    main()
