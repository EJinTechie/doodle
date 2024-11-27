import random as rd
a = range(1, 46)
data = rd.choices(a, k=100)

file_name = "ex_02.txt"
with open(file_name, "w") as file:
    for i in range(0, 100, 10):  # 0부터 90까지 10씩 증가
        line = ' '.join(str(num) for num in data[i:i+10])
        file.write(line + '\n')

print(f"출력 ({file_name}):")
with open(file_name, "r") as file:
    print(file.read())