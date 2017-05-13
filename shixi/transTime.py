#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
from time import strptime,mktime

'''转换时间到时间戳'''
def trans_time(item):
    time_set = re.search(r'\((.*?)\)',item).group()[1:-1]  # 找到括号中的字符串，然后去掉头尾两个括号
    time_array = strptime(time_set,"%a %b %d %H:%M:%S %Y")  # 把时间转化为时间戳
    time_stamp = int(mktime(time_array))
    return time_stamp

'''测试代码'''
if __name__ == '__main__':
    item = " 发信站: 水木社区 (Tue May  9 17:19:33 2017), 站内 "
    stamp = trans_time(item)
    print(stamp)

