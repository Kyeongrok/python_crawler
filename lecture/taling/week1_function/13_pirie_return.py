# 1파이어 볼, 2 파이어 월 그밖에 레벨업을 하세요
# 를 return하는 파이리를 만들어보세요
def pirie(p_skill_number):
    if(p_skill_number == 1):
        return "파이어볼"
    elif(p_skill_number == 2):
        return "파이어월"
    else:
        return "레벨업을 하세요"

print(pirie(1))
