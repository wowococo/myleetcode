from leezy import solution, Solution


class Q015(Solution):
    @solution
    def threeSum(self, nums):
        # k, i, j 分别表示三元组的第一个数、第二个数、第三个数
        if not nums: return []
        ans = []
        nums = sorted(nums)
        n = len(nums)
        for k in range(n-2):
            if k > 0 and nums[k] == nums[k-1]:
                continue
            if nums[k] > 0:
                break
            target = -nums[k]
            i = k + 1
            j = n - 1
            while i < j:
                s = nums[i] + nums[j]
                if s < target:
                    i += 1
                elif s > target:
                    j -= 1
                else:
                    ans.append([nums[k], nums[i], nums[j]])
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i-1]:
                        i += 1
                    while j > i and nums[j] == nums[j+1]:
                        j -= 1
        return ans

                    



def main():
    q = Q015()
    q.add_case(q.case([-1, 0, 1, 2, -1, -4]).assert_equal([[-1,-1,2],[-1,0,1]]))
    q.run()


if __name__ == '__main__':
    main()
