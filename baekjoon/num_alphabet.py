# 알파벳 개수, 10808번

alphabet='abcdefghijklmnopqrstuvwxyz'
answer = [0 for j in range(26)]
s=input()
for i in s:
    idx=alphabet.find(i)
    answer[idx]+=1

answer= [k for k in answer]
for l in range(26):
    print(answer[l], end=' ')