A, B = map(int,input().split())
#.split 공백 때 구분

if A > B:
    print(">")
elif A < B:
    print("<")
else:
    print("==")      