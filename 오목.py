T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(str, input()))for _ in range(N)]
    answer = "NO"
    for i in range(N):
        for j in range(N):
            if arr[i][j] == "o":
                for di, dj in [(1,0),(0,1),(1,-1),(-1,-1)]:
                    cnt = 1
                    for k in range(1,5):
                            
                        ni = i + di * k
                        nj = j + dj * k
                        if 0<= ni < N and 0<= nj < N:
                            if arr [ni][nj] == "o":
                                cnt += 1
                            else:
                                break
                    if cnt == 5:
                        answer = "YES"
                        break
    print(f'#{tc} {answer}')
