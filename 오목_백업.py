T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    arr = [list(map(str, input().split()))for _ in range(N)]
    answer = 'NO'

    for i in range(N):
        for j in range(N):
            if arr[i][j]=='O':
                di = [-1,-1,-1,0,0,1,1,1]
                dj = [-1,0,1,-1,1,-1,0,-1]
                ni = i + di[d] * 5
                nj = j + dj[d] *5
                for d in range(8):
                    if 0<= ni <N and 0<= nj <N:
                        if arr[ni][nj] =='O':
                            answer = 'YES'
    print('f#{tc} {answer}')                    

