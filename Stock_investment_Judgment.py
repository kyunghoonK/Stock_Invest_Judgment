# 고점대비 하락률

def HR(a, b):
    return (a - b)/a * 100

high = int(input("52주 최고가 : "))
now = int(input("현재가 : "))
ratio = HR(high, now)
result = "현재 고점대비 {0:0.2f}% 하락한 상태입니다.".format(ratio)

print(result)

if ratio >= 20 :
    print("항목 1 통과")
else :
    print("항목 1 X")