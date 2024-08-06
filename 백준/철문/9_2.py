# 사용자에서 주민번호를 입력 받기
rrn = input("주민번호를 입력하세요: ").replace("-","")

rrn1 = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5]
total = 0

# 주민번호의 앞 12자리를 곱하기 
for i in range(12):
    result = int(rrn[i]) * (rrn1[i])
    # 이 결과를 모두 더하기
    total +=  result

    # 더한 결과를 11로 나눈 나머지를 구하기
    remainder = total % 11
    # 11에서 이 나머지를 뺀 후 10으로 나눈 나머지 구하기
    result1 = (11 - remainder) % 10

# 결과
if result1 == int(rrn[12]):
    print("유효한 주민번호입니다")
else:
    print("유효하지 않은 주민번호입니다")

                 
  