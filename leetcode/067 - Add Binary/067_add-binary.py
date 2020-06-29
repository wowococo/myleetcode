from leezy import solution, Solution

class Q067(Solution):
    @solution
    def addBinary(self, a, b):
        return bin(int(a, 2)+int(b,2))[2:]

def main():
    q = Q067()
    q.add_case(q.case('11', '1').assert_equal('100'))
    q.add_case(q.case('1010', '1011').assert_equal("10101"))
    q.run()


if __name__ == '__main__':
    main()
