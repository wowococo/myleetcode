from leezy import solution, Solution


class Q378(Solution):
    # 196 ms faster than 87.41%, 20.4 MB less than 5.00%
    @solution
    def kthSmallest(self, matrix, k):
        arr = []
        for li in matrix:
            arr.extend(li)
        arr = sorted(arr)
        return arr[k - 1]

    @solution
    def kthSmallest2(self, matrix, k):
        # 164 ms faster than 100.00%, 20.4 MB less than 5.00%
        l, r = matrix[0][0], matrix[-1][-1] + 1
        n = len(matrix[0])
        while l < r:
            mid = l + (r - l) // 2
            total = 0
            i = n - 1
            for row in matrix:
                while i >= 0:
                    if row[i] <= mid:
                        break
                    else:
                        i -= 1
                total += i + 1
            if total >= k:
                r = mid
            else:
                l = mid + 1
        return l


def main():
    q = Q378()
    q.add_case(q.case([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8).assert_equal(13))
    q.run()


if __name__ == '__main__':
    main()
