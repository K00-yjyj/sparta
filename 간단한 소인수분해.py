T = int(input())
for tc in range(1, T +1):
    # 받는 숫자
    N = int(input())
    # 제곱 숫자 셀 카운트 만들기
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    while True: # 얼마나 반복할지 모르므로 while문
        if N % 2 == 0: # 만약에 N이 2로 나누어 떨어진다면 2로 나눈 값을 N으로 재할당
            N = N // 2
            a += 1
        elif N % 3 == 0: # 12 라인과 같이 반복복
            N = N // 3
            b += 1
        elif N % 5 == 0:
            N = N // 5
            c += 1
        elif N % 7 == 0:
            N = N // 7
            d += 1
        elif N % 11 == 0:
            N = N // 11
            e += 1
        elif N == 1:
            break
    print(f'#{tc} {a} {b} {c} {d} {e}')