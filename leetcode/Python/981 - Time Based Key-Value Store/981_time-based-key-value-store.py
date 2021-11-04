from collections import namedtuple
from bisect import bisect_right
val_time = namedtuple('val_time', ['val', 'time'])
# vals_timestamp = val_time([], []) # 全局变量影响重复使用,下次使用便不是[],[]

class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = {}  

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        # 取key之前需先判断有无key
        if key not in self.data:
            self.data[key] = val_time([value], [timestamp])
            return
        self.data[key].val.append(value)
        self.data[key].time.append(timestamp)

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        if key not in self.data:
            return ""
        i = bisect_right(self.data[key].time, timestamp)
        if i == 0:
            return ""
        else:
            return self.data[key].val[i-1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

def main():
    timemap = TimeMap()
    operations1 = ['set', 'get', 'get', 'set', 'get', 'get']
    operations2 = ["set","set","get","get","get","get","get"]
    oprands1 = [['foo', 'bar', 1], ['foo', 1], ['foo', 3], ['foo', 'bar2', 4], ['foo', 4], ['foo', 5]]
    oprands2 =  [["love","high",10],["love","low",20],["love",5],["love",10],["love",15],["love",20],["love",25]]
    for opt, opd in zip(operations1, oprands1):
        if hasattr(timemap, opt):
            print(getattr(timemap, opt).__call__(*opd))
    print('-------------')
    for opt, opd in zip(operations2, oprands2):
        if hasattr(timemap, opt):
            print(getattr(timemap, opt).__call__(*opd))


if __name__ == '__main__':
    main()
