# 테스트 케이스 받기
T = int(input())
for tc in range(1, T+1):
    N = int(input()) # 배수 되는 값 

    cnt_N = 1 # 배수되는 만큼의 값
    new_set = set() # 중복을 막기 위한 세트 설정

    while True: # 얼마나 반복될 지 모르므로 While
        num = cnt_N * N # N의 cnt_N의 배수 값

        for c in str(num): # N의 cnt_N의 배수 값을 문자열로 받아 한자리의 원소로 떼어와 세트에 넣기
            new_set.add(c)

        if len(new_set) == 10: # 들어갈 수 있는 숫자는 (0~9 )10개이기에 세트에 길이가 10이되면 멈춤
            break

        cnt_N += 1 # 멈추지 않는다면 배수될 값에 1을 더해서 반복함

    print(f'#{tc} {num}') 