# ㅌㅔ스트 케이스 받기
T = int(input())
for tc in range(1, T+1):
    N = int(input())# 증가하는 N의 크기 

    cnt_N = 1 #배수 
    new_set = set() # 중복 제외 정수 넣을 곳 

    while True: # 반복이 얼마나 돌지 모르니까
        num = cnt_N * N # 반복 한번 돌때 마다 배수 1씩 증가 시킨 N의 배수값

        for c in str(num): # 배수값을 문자열로 바꿔 원소 하나씩 나눔
            new_set.add(c) # 빈 세트에 넣어서 중복 삭제

        if len(new_set) == 10: # 원소 하나씩 넣으므로 들어갈 수 있는 크기 0~9 이므로 10이면 다 들어감
            break

        cnt_N += 1 # 브레이크 안될 경우 배수 1 증가

    print(f'#{tc} {num}')


# # 1차 실패 코드 ( 무한 대기남..)
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input()) #배수 크기 
#     cnt_N = 1
#     new_set = set () # 중복 제외 정수 넣을 곳 
#     while True:
#         cnt_N *N
#         cnt_N += 1
#         for c in str(cnt_N *N):
#             new_set.add(c)
#             if new_set in range(10):
#                 break
# print(f'#{tc} {cnt_N}')

