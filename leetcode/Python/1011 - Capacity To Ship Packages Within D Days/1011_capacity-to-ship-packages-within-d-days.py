from leezy import solution, Solution


class Q1011(Solution):
    @solution
    def shipWithinDays(self, weights, D):
        # ship capacity location
        l, r = max(weights), sum(weights) 
        # if 'while True', when weights = [x], then will enter a infinite loop
        # if l == r, then len(weights) == 1, and inifite loop
        while l < r:
            mid = l + (r - l) // 2
            day, tmp = 1, 0
            for weight in weights:
                tmp += weight
                if tmp > mid:
                    day += 1
                    tmp = weight
            if day > D:
                l = mid + 1
            else:
                r = mid
        return l
                
                



def main():
    q = Q1011()
    q.add_case(q.case([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))
    q.run()


if __name__ == '__main__':
    main()
