x,y=map(int,input("두 수를 입력 : ").split())
def sub(x,y):
    return x - y
print(f"{x}-{y} = {sub(x,y)}")

c=lambda x,y:x-y
print(f"{x}-{y} = {c(x,y)}")
