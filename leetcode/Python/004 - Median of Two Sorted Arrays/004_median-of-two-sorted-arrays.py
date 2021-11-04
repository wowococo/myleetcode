from leezy import solution, Solution


class Q004(Solution):
    @solution
    def findMedianSortedArrays(self, nums1, nums2):
        # import pdb; pdb.set_trace()
        nums = self.merge(nums1, nums2)
        print(nums)
        l, r = 0, len(nums)
        mid = l + (r - l) // 2

        return (nums[mid] + nums[mid - 1]) / 2 if len(nums) % 2 == 0 else nums[mid]
        
    def merge(self, nums1, nums2):
        res = []
        while nums1 and nums2:
            if nums1[0] > nums2[0]:
                po = nums2.pop(0)
            else:
                po = nums1.pop(0)
            res.append(po)
        if nums1: res.extend(nums1)
        if nums2: res.extend(nums2)
        return res


def main():
    q = Q004()
    q.add_case(q.case([1, 3], [2]))
    q.add_case(q.case([1, 2], [3, 4]))
    q.add_case(q.case([0, 0], [0, 0]))
    q.add_case(q.case([], [1]))
    q.add_case(q.case([2], []))
    q.add_case(q.case([3], [-2, -1]))
    q.run()


if __name__ == '__main__':
    main()
