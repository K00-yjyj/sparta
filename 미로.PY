T = int(input())
for tc in range(1, T+1):
    N = int(input()) #N*N 배열의 기준 받기
    # 이차원 배열받기 (0은 톨로 1은 벽 2는 출발 3은 도착)
    arr = [list(map(int, input()))for _ in range(N)]
    
    # 출발 위치(2인곳) 찾기
    str_i , str_j = -1, -1
    for i in range(N):
        for j in range(N):
            if arr [i][j] == 2:
                str_i, str_j = i, j
                break
    # BFS 준비 (큐, 방문배열, 방향설정)
    Q = [[str_i, str_j]] # 출발점 넣기
    visited = [[0] * N for _ in range(N)]
    visited[str_i][str_j] = 1 # 시작점 방문 표시

    answer = 0 # 기본적으로 도달 불가로 가정
    fornt = -1 # pop(0) 대신 사용할 인덱스

    # BFS 탐색 시작
    # Q가 다 떨어지면 멈추도록함
    while fornt < len(Q) - 1:
        # 다음 데이터를 확인하기
        fornt += 1
        # 다음 프론트의 값을 가지고 오기
        ci,cj = Q[fornt]
        # 목적지인지 확인
        if arr[ci][cj] == 3:
            answer = 1
            break
        # 델타 설정
        for di, dj in [(-1,0), (1,0), (0,-1), (0, 1)]:
            ni, nj = ci + di, cj + dj

            if 0<= ni <N and 0<= nj <N:
                if arr[ni][nj] !=1 and visited[ni][nj] ==0:
                    visited[ni][nj] =1 # 방문표시
                    Q.append([ni,nj])
    print(f'#{tc} {answer}')
    