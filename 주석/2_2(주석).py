# 학생들의 세 과목 점수를 입력 받아 평균 점수를 계산
# 평균에 따른 학점 등급을 부여하기 

# 사용자로부터 수학, 과학, 영어의 점수 입력 받기
math_score = float(input("수학 점수를 입력하세요: "))
science_score = float(input("과학 점수를 입력하세요: "))
english_score = float(input("영어 점수를 입력하세요: ")) 
# 입력 받은 점수 평균 점수를 계산하기 
average = (math_score + science_score + english_score) / 3

# 학점 등급
# A: 90점 이상
# B: 80점 이상 80점 미만
# C: 70점 이상 80점 미만
# D: 60점 이상 70점 미만
# F: 60점 미만

# 학점 등급 출력하기 
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
# 결과 출력하기 
print(f"평균 점수는 {average:.1f}이고, 학점은 {score}입니다. ")