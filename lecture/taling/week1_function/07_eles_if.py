# is_adult가 어른이면 안녕하세요
# is_adult가 애들이면 안녕
# is_adult가 외국인이면 hello
# 그밖에는 모르겠습니다

def exam_elif(is_adult):
    if(is_adult == "어른"):
        print("안녕하세요")
    elif(is_adult == "애들"):
        print("안녕")
    elif (is_adult == "외국인"):
        print("hello")
    else:
        print("모르겠습니다.")

exam_elif("어른")
exam_elif("애들")
exam_elif("외국인")
exam_elif("외계인")