# 감시 
# 테스트 케이스 받기
T = int(input())
for tc in range(1,T+1):
    # N * N 배열의 기준인 N 받기
    N = int(input())
    # 순회하면서 술래 위치를 좌표로 찾기 때문에 이차원배열로 정보 받기
    # 주어진 자료 공백을 가지는지 잘 확인하기!!
    # N*N 행렬이므로 range(N)으로 표현
    arr = [list(map(int, input().split()))for _ in range(N)]
    # 술래 위치 부터 잡기 위해 행우선 순회로 술래(2) 찾기
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                # 술래 위치부터 십자 모양으로 감시 가능
                # (벽은 통과 불과 + 벽 뒤는 감시 불가) 일단 전 벽을 만나면 중단이므로 술래를 만나는 경우는 감시 가능하게 함.
                # 술래 위치를 잡았다면 일단 델타를 사용해서 상하좌우 감시되는지 확인하기
                for di, dj in [(-1,0), (1,0), (0,-1), (0,1)]:
                    # 왜 1 부터 하냐하면 0은 지금 arr[i][j]이기 때문에 제외하기 위함
                    for k in range(1,N):
                        ni, nj = i + di * k, j +dj *k
                        # 여기서 저는 자주 실수해서 이제 저는 델타 이동구간(ni,nj) 만든 뒤에는
                        # 무조건 범위 지정하는 걸 습관처럼 하기로 했습니다.
                        if 0 <= ni < N and 0 <= nj < N:
                            # 범위내에서 이동할때 이제 벽을 만나면 중단 
                            if arr[ni][nj] == 1:
                                break
                            # 통로 (0)인 경우에는 값을 3로 바꿈 
                            elif arr[ni][nj] == 0:
                                arr[ni][nj] = 3
                            # 술래가 두명일 경우도 있기에 술래를 만날 경우 그냥 건너뜀
                            elif arr[ni][nj] == 2:
                                continue
    # 이제 포문과는 관계없이 결과를 내기 위해 완전히 빠져나옴
    # 안전한 영역을 셀 카운트 준비
    cnt = 0
    # 이제 위에서 수정된 이차원 배열을 돌면서 안전한 구역(0)만을 카운트 할것
    # 이경우 위에 for문과는 완전히 다른 순회이므로 같은 변수인 i와 j를 써도 무방함
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0:
                cnt += 1
    print(f'#{tc} {cnt}')

