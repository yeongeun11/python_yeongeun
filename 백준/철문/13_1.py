# 문자열 입력받기
str = input("문자열 입력: ")

# 단어 입력받기
word = input("단어 입력: ")

# 찾고자 하는 단어 세는 변수
count = 0

# 단어 저장 변수 초기화
word1 = ""

# 문자열의 각 문자 순회하기 
for char in str:
    if char == " ":
        if word1 == word:
            count += 1 

        word1 = " "
    else: 
        word1 += char

if word1 == word:
    count += 1

print(f"단어 '{word}'의 출현 빈도: {count} ")






