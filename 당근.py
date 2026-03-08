T = int(input())
for tc in range(1, T+1):
    N = int(input()) # 당근 개수
    arr = list(map(int, input(). split())) # 당근 크기 받기
    arr.sort() # 당근 크기 오름차순으로 정리하기(왜?? 당근 크기별로 포장을 3군데 하게끔하기 위함)
    min_diff = 1001 # 문제의 당근 개수가 1000이 최대이므로 그거보다 크게 잡아서 최소 차이를 확인함
    for i in range(N-2): #첫번째로 나누는 경계성 왜냐면 3군데로 나누려면 최소한 뒤에 2개는 있어야 함으로 뺌
        for j in range(i+1, N -1): # 처음에 결정된 i보다 하나 더 큰 것 부터 마찬가지로 최소한 뒤에 하나는 있어야함으로 범위 지정
            if arr[i] != arr[i+1] and arr[j] != arr[j+1]:
                #만약에 다음 당근 크기와 현재 당근 크기들이 다르면 함번 나눠보기
                s = i + 1 # 인덱스말고 당근 개수로 세기 위함
                m = j - i
                l = N - 1 - j
                cnt = [s, m, l]
                diff = max(cnt) - min(cnt) # 리스트에 가장 큰 수와 가장 작은 수를 나눠보기
                if min_diff > diff:
                    min_diff = diff
    # 포문을 다 돌았는데도 최소 차이가 처음과 같으면 값이 없으므로 포장 불가
    if min_diff == 1001:
        min_diff = -1

    print(f'#{tc} {min_diff}')
