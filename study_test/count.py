# 【报数游戏】100个人围成一圈，每个人有一个编码，编号从1开始到100。他们从1开始依次报数，报到为5的人自动退出圈圈，
# 然后下一个人接着从1开始报数，直到剩余的人数小于5。依次打印报到5出圈的人原始编号。
# 5 ， 10， 15，。。。。。100，6,   12，....
from collections import deque

def pnum():
    count = 0
    nums = list(range(1, 101))
    d = deque(nums)
    while len(d) >= 5:
        count += 1
        v = d.popleft()
        if count == 5:
            print(v)
            count = 0
        else:
            d.append(v)

def test_pnum():
    pnum()

if __name__ == "__main__":
    test_pnum()


def quick_sort():
    