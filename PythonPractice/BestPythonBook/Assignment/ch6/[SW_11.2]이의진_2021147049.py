text=input('문자열 입력하시오 : ')
words= text.split()
words_num={}
for word in words:
    if word in words_num:
        words_num[word]+=1
    else:
        words_num[word]=1
# words_num=sorted(words_num)
for word in sorted(words_num):
    print(f"{word} : {words_num[word]}")