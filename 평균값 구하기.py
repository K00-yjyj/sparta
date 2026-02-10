# 테스트 케이스 받기
T = int(input())
for tc in range(1, T+1):
    # 10개의 수 받아서 리스트 만들기
    arr = list(map(int,input().split()))
    # 길이 구하기 ( 문제에서는 10으로 주어짐)
    len_cnt = 0
    total_cnt = 0
    for i in arr:
        len_cnt += 1
        total_cnt += i
    # 정수 값으로 평균 값 구하기
    a = total_cnt/len_cnt
    b = int(total_cnt/len_cnt)
    if a - b >= 0.5 :
        b+=1

    print(f'#{tc} {b}')