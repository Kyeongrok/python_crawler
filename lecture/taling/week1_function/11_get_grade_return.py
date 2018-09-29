# 학생들 점수
# 점수(score)를 입력하면 등급(grade)이 아래와 같이 나오는
# function을 짜보세요
# >=90 A, >=80 B, >=70 C, < 70 F
# alt + j
def get_grade(p_score):
    if (p_score >= 90):
        return "A"
    elif (p_score >= 80):
        return "B"
    else:
        return "F"

grade = get_grade(90)
print(grade)
print(get_grade(90))
print(get_grade(80))
