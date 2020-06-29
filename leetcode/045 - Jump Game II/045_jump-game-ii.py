from leezy import solution, Solution


class Q045(Solution):
    @solution
    def jump_greedy(self, nums):
        # from begin to end
        end, step, max_position = 0, 0, 0
        for i in range(len(nums)-1):
            max_position = max(max_position, i + nums[i])
            if i == end:
                end = max_position
                step += 1
        return step


    @solution
    def jump(self, nums):
        # from end to begin timeout
        size = len(nums)
        if not nums or (size == 1):
            return 0
        position = size - 1
        step = 0
        while position != 0:
            for i in range(0, position):
                if nums[i] >= position - i:
                    step += 1
                    position = i
                    break
        return step


def main():
    q = Q045()
    q.add_case(q.case([2, 3, 1, 1, 4]))
    q.run()


if __name__ == '__main__':
    main()
