# 테스트 케이스 받기
T = int(input())
for tc in range(1, 1+T):
    # 10개의 수 받아와서 N에 배열함
    N = list(map(int, input().split()))
    cnt = 0
    for i in range(10):
        # 원소가 홀수라면
        if N[i] % 2 == 1:
            cnt += N[i]
    print(f'#{tc} {cnt}')