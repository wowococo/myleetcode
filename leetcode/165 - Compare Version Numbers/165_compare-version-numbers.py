from leezy import solution, Solution


class Q165(Solution):
    @solution
    def compareVersion(self, version1, version2):
        # 32ms 95%
        version1 = [int(ch) for ch in version1.split('.')]
        version2 = [int(ch) for ch in version2.split('.')]
        i, j, m, n = 0, 0, len(version1), len(version2)
        while i < m and j < n:
            if version1[i] > version2[j]:
                return 1
            elif version1[i] < version2[j]:
                return -1
            else:
                i += 1
                j += 1
        while i < m:
            if version1[i] != 0:
                return 1
            i += 1
        while j < n:
            if version2[j] != 0:
                return -1
            j += 1
        return 0


def main():
    q = Q165()
    q.add_case(q.case('1.01', '1.001').assert_equal(0))
    q.add_case(q.case('1.0', '1.00').assert_equal(0))
    q.add_case(q.case('0.1', '1.1').assert_equal(-1))
    q.add_case(q.case('1.0.1', '1').assert_equal(1))
    q.add_case(q.case('7.5.2.4', '7.5.3').assert_equal(-1))
    q.run()


if __name__ == '__main__':
    main()
