import random


choices = ['가위', '바위', '보']
cp_choices = random.choice(choices)

# 사용자 입력 받기
Rock_paper_scissors = input("가위, 바위, 보 중 하나를 선택하세요: ")

if Rock_paper_scissors not in choices:
    print("잘못된 입력입니다. 가위, 바위, 보 중에서 선택해주세요")
else:
    print(f"컴퓨터의 선택: {cp_choices}")

    if Rock_paper_scissors == cp_choices:
        result = "무승부입니다!"
    elif (Rock_paper_scissors == '가위' and cp_choices == '보') or \
        (Rock_paper_scissors == '보' and cp_choices == '바위') or \
        (Rock_paper_scissors == '바위' and cp_choices == '가위'):
        result = "당신이 이겼습니다!"
    else:
        result = "당신이 졌습니다!"
    

    print(f"결과: {result}")



