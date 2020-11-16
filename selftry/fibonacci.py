#fibonacci 재귀적 알고리즘
def fib(n):
    if(n<=1):
        return n
    else:
        return (fib(n-1)+fib(n-2));

for i in range(1, 11):
    print(i, fib(i))


#반복적 피보나치 알고리즘 - 더 효율적
def fib2(n):
    list=[]
    for i in range(0,n):
        if i<2:
            list.append(1)
        else:
            list.append(list[i-1]+list[i-2])
    return list[n-1] #n이면 out of range

n=int(input())
print(fib2(n))