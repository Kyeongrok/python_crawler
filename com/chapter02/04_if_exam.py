# 학생들 점수
# scores에 있는 점수의 등급을 매기는 if문을 짜보세요
# >=90 A, >=80 B, >=70 C, < 70 F

scores = [86, 75, 42, 98]

for score in scores:
    if score >= 90:
        print("A")
    elif score >= 80:
        print("B")
    elif score >= 70:
        print("C")
    else:
        print("F")
