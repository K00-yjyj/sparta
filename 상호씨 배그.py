T = int(input())
for tc in range(1,T+1):
    H, W = map(int, input().split())
    battleground = [list(map(int, input().split()))for _ in range(H)]
    N = int(input())
    bettle = str(input()) #길이는 N
    # 여기까지가 입력 값
    # bettle_mode = {
    #     "U":battleground[]
    # }
    # 먼저 전차 찾기 
    for i in range(H):
        for j in range(W):
            if battleground[i][j] == '<' or '>' or '^' or 'v':
                # 이제 시작 해야한다
                # 델타값 이제 줘 보자잉(상하좌우)
                di = [-1, 1, 0, 0]
                dj = [0, 0, -1, 1]
                for d in range(4):
                    # 포탄 쏠 경우 다 날려야하므로 k 받기
                    for k in range(1,N):
                        # 리스트로 만들어서 좀 더 편하게 사용
                        ni = [i + di[0], i + di[1], i + di[2], i + di[3]]
                        nj = [j + dj[0], j + dj[1], j + dj[2], j + dj[3]]
                        ni_s = [i + di[0]* k, i + di[1]* k, i + di[2]* k, i + di[3]* k]
                        nj_s = [j + dj[0]* k, j + dj[1]* k, j + dj[2]* k, j + dj[3]* k]
                        for r in range(N):
                            # 문자열 받을거임!!
                            if bettle[r] == 'U':
                                # 전차 방향 바꾸기
                                battleground[i][j] = '^'
                                # 범위 안인지 먼저 확인
                                if 0<= ni[0]< N and 0<= nj[0]<N:
                                    # 만약에 평지면 한칸 전차 이동 방향으로 이동
                                    if battleground[ni[0]][nj[0]] == '.':
                                        i = ni[0]
                                        j = nj[0]
                                    else:
                                        continue
                            # 위에랑 마찬가지
                            elif bettle[r] == 'D':
                                battleground[i][j] = 'v'
                                if 0<= ni[1]< N and 0<= nj[1]<N: 
                                    if battleground[ni[1]][nj[1]] == '.':
                                        i = ni[1]
                                        j = nj[1]
                                    else:
                                        continue
                            elif bettle[r] == 'L':
                                battleground[i][j] = '<'
                                if 0<= ni[2]< N and 0<=nj[2]<N: 
                                    if battleground[ni[2]][nj[2]] == '.':
                                        i = ni[2]
                                        j = nj[2]
                                    else:
                                        continue
                            elif bettle[r] == 'R':
                                battleground[i][j] = '>'
                                if 0<= ni[2]< N and 0<= nj[2]<N: 
                                    if battleground[ni[2]][nj[2]] == '.':
                                        i = ni[2]
                                        j = nj[2]
                                    else:
                                        continue
                            # 포탄을 쏘는 경우
                            elif bettle[r] == 'S':
                                # 전차 방향이 위라면
                                if battleground[i][j] == '^':
                                    # 포차 전용 델타 발사 하다가 벽돌벽이면 쏘고 강벽이면 멈춤
                                    if battleground[ni_s[0]][nj_s[0]] == '*':
                                        battleground[ni_s[0]][nj_s[0]] = '.'
                                        break
                                    elif battleground[ni_s[0]][nj_s[0]] == '#':
                                        break
                                    else:
                                        continue
                                # 위와 마찬가지
                                if battleground[i][j] == 'v':
                                    if battleground[ni_s[1]][nj_s[1]] == '*':
                                        battleground[ni_s[1]][nj_s[1]] = '.'
                                        break
                                    elif battleground[ni_s[1]][nj_s[1]] == '#':
                                        break
                                    else:
                                        continue
                                if battleground[i][j] == '<':
                                    if battleground[ni_s[2]][nj_s[2]] == '*':
                                        battleground[ni_s[2]][nj_s[2]] = '.'
                                        break
                                    elif battleground[ni_s[2]][nj_s[2]] == '#':
                                        break
                                    else:
                                        continue
                                if battleground[i][j] == '>':
                                    if battleground[ni_s[3]][nj_s[3]] == '*':
                                        battleground[ni_s[3]][nj_s[3]] = '.'
                                        break
                                    elif battleground[ni_s[3]][nj_s[3]] == '#':
                                        break
                                    else:
                                        continue
    print(f'#{tc} {battleground}')