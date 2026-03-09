# 테스트 케이스 수 입력
T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    
    # 깃발의 상태를 리스트로 저장
    flag = [list(map(int,input().split()))for _ in range(N)]
        
    # 최솟값을 저장할 변수 (최대 50x50 = 2500이므로 충분히 큰 값 설정)
    min_paint = 2501
    
    # 1. 흰색(W) 구역
    for i in range(0, N - 2):
        # 2. 파란색(B) 구역
        for j in range(i + 1, N - 1):
            
            # 현재 설정된 경계에서 다시 칠해야 하는 칸 수 계산
            current_paint = 0
            
            # (1) 흰색 구간
            for row in range(0, i + 1):
                for col in range(M):
                    if flag[row][col] != 'W':
                        current_paint += 1
            
            # (2) 파란색 구간
            for row in range(i + 1, j + 1):
                for col in range(M):
                    if flag[row][col] != 'B':
                        current_paint += 1
            
            # (3) 빨간색 구간
            for row in range(j + 1, N):
                for col in range(M):
                    if flag[row][col] != 'R':
                        current_paint += 1
            
            # 최솟값 갱신
            if current_paint < min_paint:
                min_paint = current_paint
                
    print(f"#{tc} {min_paint}")