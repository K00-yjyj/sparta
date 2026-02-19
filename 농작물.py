T = int(input())
for tc in range(1, T+1):
    N = int(input()) # 농장의 크기 N
    # N*N 이차원 배열
    arr = [list(map(int, input())) for _ in range(N)]
    
    mid = N // 2  # N//2 # 길이 N의 가운데 값
    total_cnt = 0
    
    # 1. 상단부 (중앙 포함)
    for i in range(mid + 1):
        # i가 0일 때 mid 한 칸, i가 1일 때 mid-1 ~ mid+1 (3칸)
        for j in range(mid - i, mid + i + 1):
            total_cnt += arr[i][j]
            
    # 2. 하단부 (중앙 아래부터)
    for i in range(mid + 1, N):
        # 중앙에서 아래로 얼마나 내려왔는지 계산 (1, 2, 3...)
        gap = i - mid
        # 내려온 만큼 양쪽 끝에서 좁혀 들어감
        for j in range(gap, N - gap):
            total_cnt += arr[i][j]
            
    print(f'#{tc} {total_cnt}')