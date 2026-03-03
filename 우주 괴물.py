T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split()))for _ in range (N)]
    di = [0,1,0,-1]
    dj = [1,0,-1,0]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr [i][j]==2: # 만약 괴물이라면
                for d in range(4):
                    for k in range(1, N):
                        ni = i + di[d] * k
                        nj = j + dj[d] * k
                
                        if 0<= ni< N and 0<= nj <N:
                            if arr[ni][nj] == 1 :
                                break
                            elif arr[ni][nj] == 0 :
                                arr[ni][nj] =1
                            elif arr[ni][nj] == 2 :
                                continue
                        else:
                            break
    for r in range(N):
        for c in range(N):
            if arr[r][c]==0:
                cnt += 1
    print(f'#{tc} {cnt}')