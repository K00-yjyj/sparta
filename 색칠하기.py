
# # 테스트 케이스 받기
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input()) # 색칠 영역 번호 받기
#     # 문제에서 제시한 10*10 배열 만들기
#     basic_arr = [[0]*10 for _ in range(10)]
#     # 주어진 데이터를 순서대로 받기 색칠 영역 번호(개수?)만큼 반복
#     for i in range(N):
#         i1, j1, i2, j2, color = map(int, input().split())
#         # 행 우선 순회 해서 해당칸에 컬러 색에 맞는 값 더하기(빨:1, 파:2, 보:3)
#         for i in range(i1, i2+1):
#             for j in range(j1, j2+1):
#                 basic_arr[i][j] += color

#     # 보라색(=3) 칸 세기
#     purple = 0
#     for i in range(10):
#         for j in range(10):
#             if basic_arr[i][j] == 3:
#                 purple += 1

#     print(f"#{tc} {purple}")

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

