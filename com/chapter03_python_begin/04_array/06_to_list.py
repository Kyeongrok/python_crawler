# >=90 A, >=80 B, >=70 C, < 70 F
# 를 return하는 ƒunction

scores = [79, 80, 81]
score = scores[0]

def get_grade(score):
    # >=90 A, >=80 B, >=70 C, < 70 F
    if score >=90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score < 70:
        return "F"
    else:
        return "nothing"

results = [get_grade(79), get_grade(80), "B"]
print(results)
