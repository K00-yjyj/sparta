T = int(input())
for tc in range(1,T+1):
    N = int(input())
    # 문제에서 주어진 10*10 배열 만들기
    arr = [[0]*10 for _ in range(10)]
    # 인풋값을 다음과 같이 받기 N번 반복
    for _ in range(N):
        i1,j1,i2,j2,color = map(int,input().split())
        # 행우선 순회하면 범위에 맞는 색칠하기 (누적)
        for r in range(i1,i2+1):
            for c in range(j1,j2+1):
                arr[r][c] += color
            
    # 보라색 구간 찾기
    cnt = 0
    for r in range(10):
        for c in range(10):
            if arr[r][c] == 3:
                cnt +=1
    print(f'#{tc} {cnt}')            