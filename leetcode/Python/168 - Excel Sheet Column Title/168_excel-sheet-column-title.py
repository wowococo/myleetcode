from leezy import solution, Solution


class Q168(Solution):
    @solution
    def convertToTitle(self, n): 
        s = ''
        while n:
            n -= 1
            s = chr(n%26 + 65) + s
            n = n // 26
        return s
        




def main():
    q = Q168()
    q.add_case(q.case(1).assert_equal('A'))
    q.add_case(q.case(701).assert_equal('ZY'))
    q.add_case(q.case(28).assert_equal('AB'))
    q.add_case(q.case(52).assert_equal('AZ'))
    q.run()

if __name__ == '__main__':
    main()
