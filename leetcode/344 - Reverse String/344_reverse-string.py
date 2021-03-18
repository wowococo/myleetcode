from leezy import solution, Solution


class Q344(Solution):
    @solution
    def reverseString(self, s):
        # 68 ms 8.48%
        n = len(s)
        i = 0
        j = n-i-1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        return s


def main():
    q = Q344()
    q.add_case(q.case(['h', 'e', 'l', 'l', 'o']).assert_equal(["o","l","l","e","h"]))
    q.add_case(q.case(["H","a","n","n","a","h"]).assert_equal(["h","a","n","n","a","H"]))
    q.run()


if __name__ == '__main__':
    main()
