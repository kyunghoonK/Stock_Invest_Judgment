Score = 0

# 시장 점유율 (독과점 여부) / 25점
print("===== 시장 점유율 (독과점 여부) =====")
MarkerShare = int(input("""
해당 기업이 해당 분야 3등 안에 있는 기업이고, 3등까지의 기업들이 시장 점유율 50% 이상을 차지 합니까?
yes -> 숫자 1 입력 / no -> 숫자 2 입력
"""))

if MarkerShare == 1 :
    Score += 25
else:
    Score += 0

print()

# 매출 총이익 / 25점
print("===== 매출 총 이익률 =====")
GrossProfitMarginRatio = int(input("매출 총 이익률 : "))

if GrossProfitMarginRatio >= 30 :
    Score += 25
elif 25 < GrossProfitMarginRatio  and GrossProfitMarginRatio < 30 :
    Score += 15
elif 20 < GrossProfitMarginRatio  and GrossProfitMarginRatio < 30 :
    Score += 10

print()

# 고점대비 하락률 / 25점
print("===== 고점대비 하략률 =====")
def HR(a, b):
    return (a - b)/a * 100

high = int(input("52주 최고가 : "))
now = int(input("현재가 : "))

ratio = HR(high, now)
result = "현재 고점대비 {0:0.2f}% 하락한 상태입니다.".format(ratio)

print(result)

if ratio >= 20 :
    Score = Score + 25
elif 15 <= ratio < 20 :
    Score = Score + 20
elif 10 <= ratio < 15 :
    Score = Score + 15
else :
    Score = Score + 0

print()

# PER / 25점
print("===== PER =====")
PER = int(input("현재 PER 값 : "))

if PER <= 0 :
    Score = Score + 0
elif 0 < PER <= 10 :
    Score = Score + 25
elif 10 < PER <= 20 :
    Score = Score + 20
elif 20 < PER <= 30 :
    Score = Score + 15
else :
    Score = Score + 0

print()
print()

print("==============================")
print()
print(" 종합 평가 점수 : ",Score, "점")
print()
