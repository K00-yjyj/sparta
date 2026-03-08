# X = 활주로의 길이, 높이는 1로 일정
# for문으로 순회하면서 숫자가 다른 곳이 있으면 X만큼 해서 숫자가 하나만 차이난다면 ( 활주로 번호 : 0 으로 바꾸기, 0 인 곳은 걸들지 않기)
# 지금건 오답 => 나중에 수정 코드 다시 짜볼것!!

T = int(input())
for tc in range(1, T+1):
    N, X = map(int, input())
    arr = [list(map(int, input().split()))for _ in range(N)]
    cnt = 0

    di = [-1, 1, 0, 0]
    dj = [0, 0,-1, 1]
    for i in range(N):
        for j in range(N):
            for d in range(4):
                for k in range(1,X):
                    ni = i + di[d] * k
                    nj = j + dj[d] * k
                    if 0 <= ni < N and 0 <= nj < N :
                        if arr[i][j] -1 == arr[ni][nj] or arr[i][j] + 1 == arr[ni][nj]:
                            if arr[ni][nj] != 0:
                                arr[ni][nj] = 0
                                cnt += 1
    print(f'#{tc} {cnt}')
        


