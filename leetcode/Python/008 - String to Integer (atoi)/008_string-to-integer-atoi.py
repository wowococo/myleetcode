from leezy import solution, Solution


class Q008(Solution):
    @solution
    def myAtoi(self, s):
        s = s.strip()
        # empty
        if len(s) == 0:
            return 0
        
        # neg or pos
        flag = 1
        if s[0] in '-+':
            flag = -1 if s[0] == '-' else 1
            s = s[1:]

        MAX, MIN = 2 ** 31 - 1, -(2 ** 31)
        M, R = divmod(MAX, 10)   # 不能用 -MIN， -MIN 求的 R是 8，正数是从 > 7 开始溢出的

        ans = 0
        for ch in s:
            if ch.isdigit():
                v = int(ch)
                if ans > M or (ans == M and v > R):
                    return MAX if flag > 0 else MIN
                ans = ans * 10 + v
            else:
                break
            
        return flag * ans



def main():
    q = Q008()
    q.add_case(q.case('42').assert_equal(42))
    q.add_case(q.case('-42').assert_equal(-42))
    q.add_case(q.case('4193 with words').assert_equal(4193))
    q.add_case(q.case('words and 987').assert_equal(0))
    q.add_case(q.case('-91283472332').assert_equal(-2147483648))
    q.add_case(q.case('4193 with 345').assert_equal(4193))
    q.add_case(q.case("2147483648").assert_equal(2147483647))
    q.run()


if __name__ == '__main__':
    main()
