T = int(input())
for tc in range(1,T+1):
    N, M ,K = map(int,input().split())
    # N명
    # M초마다 K개씩 만듦
    # 도착하면 N명이 해당하는 초에 다 먹을 수 있는 그니까 N의 도착시간에 =<K 개가 되는지
    # 그러면 일단 사람이 도착하는 시간이 M보다 작으면 바로 먹지 못함 "Impossible"
    # 사람이 도착하는 시간이 M보다 크고 K가 1보다 크다면 "Possible"
    # N 명의 사람이 도착하는 시간을 받고 빨리 오는 순서대로 나열하기
    answer = "Possible"
    time = list(map(int,input().split()))
    time.sort()

    for people in range(N):
        bbang = (time[people]//M) * K
        if bbang < (people + 1):
            # 만약 빵 갯수가 지금까지 온사람( 인덱스 개수) 보다 작으면 실패
            answer = "Impossible"
            break
    print(f'#{tc} {answer}') 
