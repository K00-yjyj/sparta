T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    # 수열이 작은 값이 이동가능 함
    # 이동하는 수열의 0번 인덱스가 갈 수 있는 구간은 두 수열의 차의 절댓값 +1
    # 더 길이가 작은 수열 구하기
    if N <= M:
        min_lst = A
        max_lst = B
    if N > M:
        min_lst = B
        max_lst = A
    total_cnt = 0 # 정답 답
    
    for i in range(abs(N-M)+1):
        cnt = 0
        for n in range(len(min_lst)):
            cnt += min_lst[n]*max_lst[i + n]
        if total_cnt<cnt:
            total_cnt = cnt
    print(f'#{tc} {total_cnt}')


