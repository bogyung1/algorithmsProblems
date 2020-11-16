# 순차탐색
def search_list(a,x):
    n=len(a)
    result=[]
    for i in range(0,n):
        if x==a[i]:
            result.append(i)
    return result;

s= [8, 3, 4, 5, 1, 9, 6, 7, 2, 0];
x=8;
print(search_list(s, x))

# 오름차순 정렬
print('오름차순')
s.sort()
print(s)
# 내림차순, 역순정렬
new_list=sorted(s, reverse=True)
print('new_list', new_list)
