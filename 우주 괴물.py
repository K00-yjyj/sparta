T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split()))for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr [i][j] == 2:
                for di,dj in [(-1,0), (1,0), (0,-1),(0,1)]:
                    ni, nj = i+di, j+dj
                    while 0<= ni < N and 0<= nj < N:
                        if arr [ni][nj] == 1:
                            break
                        elif arr [ni][nj] == 0:
                            arr[ni][nj]=1
                        elif arr[ni][nj] == 2:
                            continue
                        ni += di
                        nj += dj
    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0:
                cnt += 1
    print(f'#{tc} {cnt}')