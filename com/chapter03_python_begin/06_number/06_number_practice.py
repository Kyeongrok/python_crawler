cheolsu_kor = 88
cheolsu_eng = 76
cheolsu_math = 95
younghee_kor = 100
younghee_eng = 67
younghee_math = 80

cheolsu_average = (cheolsu_kor + cheolsu_eng + cheolsu_math) / 3
younghee_average = (younghee_kor + younghee_eng + younghee_math) / 3

if (cheolsu_average > younghee_average):
    print("철수가 높아요")
elif (cheolsu_average == younghee_average):
    print("둘이 같아요")
else:
    print("영희가 높아요")
