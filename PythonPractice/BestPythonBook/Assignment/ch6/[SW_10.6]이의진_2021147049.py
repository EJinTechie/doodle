text=input('문자열 입력하시오 : ')
words= text.split()
words_num={}
for word in words:
    if word in words_num:
        words_num[word]+=1
    else:
        words_num[word]=1
# print(list(words_num.keys()))
dup=0
without_dup=0
for word in words_num:
    if words_num[word]>1:
        dup+=1
    if words_num[word]>0:
        without_dup+=1
print(words)
print(dup+without_dup)
print(list(words_num.keys()))
print(without_dup)