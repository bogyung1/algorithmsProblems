# 시간초 초과
# 시간초과 에러 --> sys.stdin.readline()을 input()대신 써야한다.
import sys

# n=int(input())
n=int(sys.stdin.readline())
stack=[]

for i in range(n):
    value=sys.stdin.readline().split()
    if value[0]=='push':
        stack.append(value[1]);
    elif value[0]=='pop':
        if not stack:
            print('-1')
        else:
            print(stack[-1])
            stack.pop(-1)
    elif value[0]=='size':
        print(len(stack))
    elif value[0]=='empty':
        if len(stack)==0:
            print('1')
        else:
            print('0')
    elif value[0]=='top':
        if not stack:
            print('-1')
        else:
            print(stack[-1])
