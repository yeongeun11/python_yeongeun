menus = ["피자", "파스타", "샐러드", "스시", "버거"]

# 사용자에게 인덱스를 입력 받기
index = int(input("메뉴의 덱스를 선택하세요 (0부터 시작): "))

if 0 <= index < len(menus):
    print(f"선택된 메뉴: {menus[index]}")
else:
    print("유효하지 않은 선택입니다.")