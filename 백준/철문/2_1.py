# 제곱미터(m²)를 평방비트(ft²)로 변환하는 함수
def convert_to_square_feet(square_meters):
    return  square_meters * 10.7639
# 에이커(ac)를 제곱미터(m²)로 변환하는 함수
def convent_to_acers(square_meters):
    return square_meters / 4046.86

# 사용자 입력  받기
square_meters = float(input("토지의 면적을 제곱미터(m²) 단위로 입력하세요: "))

if square_meters > 0:
    print(f"{square_meters} 제곱미터는 {convert_to_square_feet(square_meters)} 평방비트입니다.")
    print(f"{square_meters} 제곱미터는 {convent_to_acers(square_meters)} 에이커입니다.")
else:
    print("잘못된 입력입니다.")