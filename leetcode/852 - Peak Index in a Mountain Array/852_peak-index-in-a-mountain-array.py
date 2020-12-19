from leezy import solution, Solution


class Q852(Solution):
    @solution

    def peakIndexInMountainArray(self, arr):
        # 40 ms faster than 79.34%, 15.7 MB less than 5.77%
        l, r = 0, len(arr) - 1
        while l < r:
            mid = l + (r - l) // 2
            if arr[mid] > arr[mid + 1]:
                r = mid
            else:
                l = mid + 1
        return l


def main():
    q = Q852()
    q.add_case(q.case([0, 1, 0]).assert_equal(1))
    q.add_case(q.case([0, 2, 1, 0]).assert_equal(1))
    q.run()


if __name__ == '__main__':
    main()
