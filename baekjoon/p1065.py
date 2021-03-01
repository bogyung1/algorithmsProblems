# 1065번, 한수
# 한수: 어떤 양의 수 정수 num가 각 자리가 등차수열을 이룬 수

num=int(input()) #어떤 수
hansu=0 

for n in range(1, num+1):
    if n<100: #1~99까지는 모두 한수
        hansu+=1

    else:
        nums=list(map(int, str(n))) #숫자를 자릿수대로 분리
        if nums[0]-nums[1]== nums[1]-nums[2]: #등차수열 규칙
            hansu+=1