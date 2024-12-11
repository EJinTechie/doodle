import random as rd
sentence=list(input('문자열 입력 : ').split())
print(sentence)
sentence1=sentence.copy()
rd.shuffle(sentence1)
print(sentence1)

cnt=0
for i in range(len(sentence)):
    if sentence[i]==sentence1[i]:
        cnt+=1
print(cnt)