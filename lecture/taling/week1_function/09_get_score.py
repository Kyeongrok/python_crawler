# 학생들 점수
# score에 있는 점수의 등급을 매기는 if문을 짜보세요
# >=90 A, >=80 B, >=70 C, < 70 F

def get_grade(p_score):
    if(p_score >= 90):
        print("A")
    elif(p_score >= 80):
        print("B")
    else:
        print("F")

get_grade(95)
get_grade(90)
get_grade(85)
get_grade(80)
get_grade(70)
get_grade(60)