# N = int(input())
# # 스위치 상태 (on:1,off:0)
# arr = list(map(int, input().split()))
# # 학생수
# std = int(input())
# # 학생 성별(남:1, 여:2)
# std_x =[list(map(int, input().split()))for _ in range(std)]
# for i in range(N):
#     for j in range(2):
#         # 만약 남자 아이라면
#         if std_x[i][0] == 1:
#             for idx in range(len(arr)):
#                 if(idx+1) % (std_x[i][1]+1) == 0:
#                     if arr [idx + 1] == 0:
#                         arr[idx + 1] = 1
#                     elif arr[idx + 1] == 1:
#                         arr[idx + 1] = 0
#         # 만약 여자 아이라면?
#         if std_x[i][0] == 2:
#             # 여자아이가 받은 스위치 번호 
#             if arr[std_x[i][1]+1] == 0:
#                 arr[std_x[i][1]+1] =1
#             elif arr[std_x[i][1]+1] ==1:
#                 arr[std_x[i][1]+1] =0
#                 for diff in range(std_x[i][i]):
#                     if arr[std_x[i][1] + 1 - diff] == arr[std_x[i][1] + 1 + diff]:
#                         if arr[std_x[i][1] + 1 - diff] == 0:
#                             arr[std_x[i][1] + 1 - diff] = 1
#                             arr[std_x[i][1] + 1 + diff] = 1
#                         elif arr[std_x[i][1] + 1 - diff] == 1:
#                             arr[std_x[i][1] + 1 - diff] = 0
#                             arr[std_x[i][1] + 1 + diff] = 0
# print (arr)

N = int(input())
arr = list(map(int, input().split()))
std = int(input())
std_x = [list(map(int, input().split())) for _ in range(std)]

# 1. 반복문은 학생 수만큼
for i in range(std):
    # 남학생
    if std_x[i][0] == 1:
        val = std_x[i][1] # 받은 숫자
        for idx in range(len(arr)):
            # idx+1이 배수인지 확인 
            if (idx + 1) % val == 0:
                if arr[idx] == 0: # arr[idx+1]은 범위를 벗어남
                    arr[idx] = 1
                elif arr[idx] == 1:
                    arr[idx] = 0
    
    # 여학생
    if std_x[i][0] == 2:
        center = std_x[i][1] - 1 
        # 자기 자신 반전
        if arr[center] == 0: arr[center] = 1
        else: arr[center] = 0
        
        # 좌우 대칭 확인 
        for diff in range(1, N):
            # 범위 지정
            if center - diff < 0 or center + diff >= N:
                break
            
            if arr[center - diff] == arr[center + diff]:
                if arr[center - diff] == 0:
                    arr[center - diff] = 1
                    arr[center + diff] = 1
                else:
                    arr[center - diff] = 0
                    arr[center + diff] = 0
                

# 출력 포맷 수정 (AI사용 부분)
for k in range(N):
    print(arr[k], end=" ")
    if (k + 1) % 20 == 0:
        print()