# N = int(input()) # 정사각형 크기
# # 이번 문제를 푸는 방법
# # 행우선 순회로 2차원 배열 순회하다가 1을 만나면 cnt+=1로 두기
# # 1과 연결된 1들을 따라다니며 0처리 연결된 모든 1이 끝나면 다시 3번 줄로 돌아가기
# # 반복하다가 모든 배열이 0이 됐을때 cnt 를 답으로 제출
# arr = [list(map(int, input()))for _ in range(N)]
# # 델타 탐색
# di = [-1,1,0,0]
# dj = [0,0,1,-1]

# def find_apt(i, j):
    
#     # 현재 위치를 방문처리(0으로 지우기)
#     arr[i][j] = 0
#     cnt = 1 # 현재 집 카운트

#     for d in range(4):
#         ni = i + di[d]
#         nj = j + dj[d]

#         # 지도 범위 내에 있고, 아직 1인 곳으로만 이동하게 하기
#         if 0 <= ni < N and 0 <= nj <N:
#             if arr[ni][nj] == 1:
#                 cnt += find_apt(ni,nj)
#     return cnt # 한 단지에서 찾은 총 집 갯수

# main_cnt = [] # 단지별 집 개수 담기
# for i in range(N):
#     for j in range(N):
#         if arr[i][j] == 1 :
#             apt_cnt = find_apt(i,j)
#             main_cnt.append(apt_cnt)

# main_cnt.sort()
# print(len(main_cnt))
# for cnt in main_cnt :
#     print(cnt)



N = int(input())
arr = [list(map(int, input()))for _ in range(N)]

di = [0,0,-1,1]
dj = [1,-1,0,0]

def find_apt (i,j):
    arr [i][j] = 0
    cnt = 1
    
    for d in range(4):
        ni = i + di[d]
        nj = j + dj[d] 
        if 0<= ni < N and 0<= nj < N:
            if arr [ni][nj] == 1:
                cnt += find_apt(ni, nj)
    return cnt

main_apt = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            main_apt.append(find_apt)

main_apt.sort()
print(len(main_apt))

for h in main_apt:
    print(h)


                                