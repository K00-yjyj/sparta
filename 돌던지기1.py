T = int(input())  # 전체 게임(테스트 케이스) 개수

for tc in range(1, T + 1):
    # N: 돌의 개수, M: 뒤집기 명령 횟수
    N, M = map(int, input().split())
    # s: 돌의 초기 상태 리스트
    s = list(map(int, input().split()))

    for _ in range(M):
        # i: 시작 위치, j: 뒤집을 돌의 개수
        i, j = map(int, input().split())
        
        # 1. 기준이 되는 i번째 돌의 색깔을 먼저 확인합니다. (리스트는 0번 인덱스부터 시작하므로 i-1)
        target_color = s[i-1]
        
        # 2. i번째(인덱스 i-1)부터 j개를 바꿔야 하므로 반복 범위를 설정합니다.
        # 범위를 벗어날 수 있으므로 min 함수로 안전하게 끝 지점을 정합니다.
        start = i - 1
        end = min(i - 1 + j, N)
        
        for k in range(start, end):
            # 전구 문제처럼 if-elif 구조를 사용하여 색깔을 변경합니다.
            if target_color == 0:  # 기준 색깔이 흰색(0)이면
                s[k] = 0           # 범위를 모두 흰색으로 변경
            elif target_color == 1: # 기준 색깔이 검은색(1)이면
                s[k] = 1           # 범위를 모두 검은색으로 변경

    # 결과 출력 (#번호 돌상태)
    print(f"#{tc}", *s)