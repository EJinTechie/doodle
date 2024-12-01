data=input("data 입력 : ")
data_list=data.split()
file_name="ex_01.txt"

with open(file_name, "w") as file:
    for item in data_list:
        file.write(item + "\n")

print(f"출력:")
with open(file_name, "r") as file:
    print(file.read())