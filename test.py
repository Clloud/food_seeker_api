# -*- coding: utf-8 -*-
'''
@author: Cloud
@time: 2019/1/27 20:28
'''

class A:
    a = 1
    b = 2
    c = 3

print(A.__dict__)

# A = {
#     'a':1,
#     'b':2,
#     'c':3
# }

if not isinstance(A, dict):
    for i in A.__dict__:
        print(getattr(A,i))

# for i in dir(A):
#     print(i)