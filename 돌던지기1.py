T = int(input())  # 게임의 개수

for tc in range(1, T + 1):
    # N = 돌의 개수, M = 뒤집기 횟수
    N, M = map(int, input().split())
    # 돌의 초기 상태 받기 (리스트 형태로 저장)
    s = list(map(int, input().split()))

    for _ in range(M):
        # i = 시작 위치(1부터 시작), j = 뒤집을 개수
        i, j = map(int, input().split())
        
        # 1. 기준이 되는 i번째 돌의 색깔 확인하기
        # 리스트 인덱스는 0부터 시작하므로 i-1 위치의 값을 가져옴
        target_color = s[i-1]
        
        # 2. i번째부터 j개의 돌을 기준 색깔(target_color)로 바꾸기
        # 시작 인덱스는 i-1, 끝 인덱스는 (시작 + 개수)인 i-1 + j
        # 단, 범위를 벗어나면 안 되므로 min(i-1 + j, N)을 사용
        end_index = min(i - 1 + j, N)
        
        for k in range(i - 1, end_index):
            s[k] = target_color


    print(f"#{tc}", *s)