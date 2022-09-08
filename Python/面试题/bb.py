 ## 请在下方进行输入 ( 支持Markdown、插入公式及 LaTex 数学公式，点击上方按钮“环境说明”查看详情 )

# ## ES 搜索实现的原理

# ## 采集

# 文件, 执行命令, logstash

# ## 处理

# 正则

# 电话号码(国内)

# 139-9999-9999
import re
from typing import Pattern 

def ismatch(express, s):
    m = re.match(express, s)
    return m
  
if __name__ == "__main__":
    s1 = "13999999999"
    s2 = "021-23456789"
    Pattern = r"(1\d{10})|(\d{3}-\d{8}(-\d{4})?)"
    res1 = ismatch(Pattern, s1)
    res2 = ismatch(Pattern, s2)
    print(res1, res2)
  
  # decorate
  
  # """
  # 实现装饰器
  # 打印函数的执行耗费的时间
  # print
  # """
import time
  
def log(func):
    def wrapper(*args, **kwargs):
        t1 = time.perf_counter()
        res = func(*args, **kwargs)
        t2 = time.perf_counter()
        print("cost time %.2f seconds" % (t2-t1))
        return res

    return wrapper
  
@log
def add_two_num(x, y):
    time.sleep(2)
    return x + y

@log
def add_three_num(x, y , z):
    return x + y + z


if __name__ == "__main__":
    ret = add_two_num(3, 5)
    ret = add_three_num(1, 2, 3)
    print(ret)
  
  