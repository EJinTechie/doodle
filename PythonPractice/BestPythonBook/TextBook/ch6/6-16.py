student_tuple=(('191101','홍길동', '010-1234-2518'),('191102','임꺽정','010-4684-6516'),('191103','장길산','010-6548-5466'))
student_dict={student[0]:student[1] for student in student_tuple}

print(f"학생 정보 : {student_dict}")
a=0
while a!='-1':
    a = input("학번을 입력하세요 : ")
    if a in student_dict.keys():
        print(f"{a}번 학생은 {student_dict[a]}")
    else:
        print("해당 학번의 학생이 없습니다")
if a== '-1':
    print("프로그램을 종료합니다.")