# 덱, 10866번
# double ended queue
# 이중연결리스트같은 구조
from collections import deque
import sys

d=int(sys.stdin.readline())
deque=[]

for i in range(d):
    value=sys.stdin.readline().split()
    if value[0]=="push_front":
        deque.insert(0, value[1])
    elif value[0]=="push_back":
        deque.append(value[1])
    elif value[0]=='pop_front':
        if not deque:
            print('-1')
        else:
            print(deque.pop(0))
    elif value[0]=='pop_back':
        if not deque:
            print('-1')
        else:
            print(deque.pop(-1))
    elif value[0]=='size':
        print(len(deque))
    elif value[0]=='empty':
        if len(deque)==0:
            print('1')
        else:
            print('0')
    elif value[0]=='front':
        if not deque:
            print('-1')
        else:
            print(deque[0])
    elif value[0]=='back':
        if not deque:
            print('-1')
        else:
            print(deque[-1])


