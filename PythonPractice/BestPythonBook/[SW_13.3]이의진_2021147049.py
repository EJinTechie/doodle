import random as rd

frequency = [0] * 45
print("\n빈도수 카운트 전")
print(frequency)

a = range(1, 46)
data = rd.choices(a, k=100)

file_name = "ex_02.txt"
with open(file_name, "w") as file:
    for i in range(0, 100, 10):
        line = ' '.join(str(num) for num in data[i:i+10])
        file.write(line + '\n')

with open(file_name, "r") as file:
    print(file.read())



for num in data:
    frequency[num-1] += 1

print("빈도수 카운트 후")
print(frequency)