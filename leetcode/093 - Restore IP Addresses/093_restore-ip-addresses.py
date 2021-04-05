from leezy import solution, Solution


class Q093(Solution):
    @solution
    def restoreIpAddresses(self, s):
        # combination template
        cur, total = [], []
        def dfs(n, start):
            if n == 4 and start == len(s):
                total.append(".".join(cur))
                return
            if n > 4 or start >= len(s):
                return
            for i in range(start, min(len(s), start+3)):
                part = s[start:i+1]
                if len(part) > 1 and part[0] == "0":
                    return
                if int(part) > 255:
                    return
                cur.append(part)
                dfs(n+1, i+1)
                cur.pop()

        dfs(0, 0)
        return total 


def main():
    q = Q093()
    q.add_case(q.case('25525511135').assert_equal(["255.255.11.135","255.255.111.35"]))
    q.run()


if __name__ == '__main__':
    main()
