from leezy import solution, Solution


class Q459(Solution):
    @solution
    def repeatedSubstringPattern(self, s):
        t = s + s
        t1 = t[1:-1]
        if s in t1:
            return True
        else:
            return False

def main():
    q = Q459()
    q.add_case(q.case('abab'))
    q.add_case(q.case('aba'))
    q.add_case(q.case('abcabcabc'))
    q.run()


if __name__ == '__main__':
    main()
