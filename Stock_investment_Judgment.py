Score = 0

# 항목 1) 고점대비 하락률

def HR(a, b):
    return (a - b)/a * 100

high = int(input("52주 최고가 : "))
now = int(input("현재가 : "))

PER = int(input("현재 PER 값 : "))

ratio = HR(high, now)
result = "현재 고점대비 {0:0.2f}% 하락한 상태입니다.".format(ratio)

print(result)

if ratio >= 20 :
    print("항목 1 / +50 점")
    Score = Score + 50
elif 15 <= ratio < 20 :
    print("항목 1 / +35 점")
    Score = Score + 35
elif 10 <= ratio < 15 :
    print("항목 1 / +20 점")
    Score = Score + 20
else :
    print("항목 1 / -----")


# 항목 2) PER

if PER <= 0 :
    print("항목 2 / -----")
elif 0 < PER <= 10 :
    print("항목 2 / +50 점")
    Score = Score + 50
elif 10 < PER <= 20 :
    print("항목 2 / +35 점")
    Score = Score + 35
elif 20 < PER <= 30 :
    print("항목 2 / +20 점")
    Score = Score + 20
else :
    print("항목 2 / 고평가로 보여집니다.")

print(" 종합 평가 점수 : ",Score, "점")