T = 10
for tc in range(1,T+1):
    tc = int(input())
    N = 16
    arr = [list(map(int, input()))for _ in range(N)]

    # 시작점 찾기
    s_i, s_j = -1, -1
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                s_i, s_j = i, j
                break
    
    # BFS 준비
    q = [[s_i,s_j]]
    visited = [[0]*N for _ in range(N)]
    visited[s_i][s_j] = 1 # 시작점은 방문 처리

    answer = 0 # 일단 도착 불가로 두기
    front = -1 # pop(0) 대신 할 인덱스

    # BFS 시작
    while front < len(q) - 1:
        front += 1
        ci, cj = q[front]
        if arr[ci][cj] == 3:
            answer = 1
            break
        # 델타 검색
        for di, dj in [(-1,0), (1,0), (0,-1), (0,1)]:
            ni, nj = ci + di, cj + dj
            if 0<= ni < N and 0<= nj < N:
                if arr[ni][nj] != 1 and visited[ni][nj] == 0:
                    visited[ni][nj] = 1
                    q.append([ni,nj])
    print(f'#{tc} {answer}')