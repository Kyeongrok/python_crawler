def get_grade(score):
    #score>=90 A score>=80 B score>=70 C F
    if score>=90:
        print("A")
    elif score>=80:
        print("B")
    elif score>=70:
        print("C")
    else:
        print("F")

# 86, 90, 75, 32
get_grade(86)
get_grade(90)
get_grade(75)
get_grade(32)