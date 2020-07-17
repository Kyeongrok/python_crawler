def get_grade(score):
    # score를 넣으면 grade
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    else:
        return "F"

def plus_ipnida(grade):
    # grade를 넣으면 입니다. 를 붙여줌
    return grade + "입니다."

# g o f(80) = g(f(80))
# result = B입니다.
result = plus_ipnida(get_grade(80))
print(result)