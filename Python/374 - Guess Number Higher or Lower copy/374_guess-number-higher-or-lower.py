from leezy import solution, Solution


class Q374(Solution):
    @solution
    def guessNumber(self, n):
        l, r = 1, n
        while l < r:
            mid = l + (r - l) // 2
            print(l, r, mid)
            if guess(mid) == 1:
                l = mid + 1
            else:
                r = mid
            return r

def main():
    q = Q374()
    q.add_case(q.case(10))
    q.run()


if __name__ == '__main__':
    main()
