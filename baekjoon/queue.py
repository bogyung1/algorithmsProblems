
import sys

q=int(sys.stdin.readline())
queue=[]

for i in range(q):
    value=sys.stdin.readline().split()
    if value[0]=="push":
        queue.insert(0, value[1]);
    elif value[0]=='pop':
        if not queue:
            print('-1')
        else:
            # print(queue[-1])
            print(queue.pop())
    elif value[0]=='size':
        print(len(queue))
    elif value[0]=='empty':
        if len(queue)==0:
            print('1')
        else:
            print('0')
    elif value[0]=='front':
        if not queue:
            print('-1')
        else:
            print(queue[len(queue)-1])
    elif value[0]=='back':
        if not queue:
            print('-1')
        else:
            print(queue[0])


