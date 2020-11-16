#실행안됨, 왜?
def sumArray(n, s):
    result=0
    for i in range(n):
        result=result+s[i]
    return result

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
n=len(list)
sumArray(n,list);

# 두줄로 마무으리
result=sum(list)
print(result)

# 교환정렬, 비내림차순(오름차순)
def exchangeSort(n, s):
    for i in range(n):
        j=i+1
        for j in range(n):
            if(s[j]>s[i]):
                temp=s[i]
                s[i]=s[j]
                s[j]=temp

                print(s)
n= 5
s=[1,3,2,6,7]
exchangeSort(n, s)
