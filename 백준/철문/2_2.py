# 세 과목 점수를 입력 받아 평균 점수 계산
math_score = float(input("수학 점수를 입력하세요: "))
science_score = float(input("과학 점수를 입력하세요: "))
english_score = float(input("영어 점수를 입력하세요: "))

average = (math_score + science_score + english_score) / 3

if average >= 90:
    score = "A"
elif average >= 80:
    score = "B"
elif average >= 70:
    score = "C"
elif average >= 60:
    score = "D"
else:
    score = "F"

print(f"평균 점수는 {average:.1f}점이고, 학점은 {score}입니다. ")    
# :.1f