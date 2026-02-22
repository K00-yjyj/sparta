T = int(input())  # 테스트 케이스 개수

for tc in range(1, T + 1):
    # N: 돌의 수, M: 뒤집기 횟수
    N, M = map(int, input().split())
    # s: 돌의 초기 상태 (0: 흰색, 1: 검은색 등)
    s = list(map(int, input().split()))

    for _ in range(M):
        # i: 기준 돌 번호, j: 확장할 거리
        i, j = map(int, input().split())
        
        # 실제 리스트 인덱스는 i-1
        center = i - 1
        
        # 1부터 j까지 거리를 넓혀가며 확인
        for k in range(1, j + 1):
            left = center - k
            right = center + k
            
            # 범위를 벗어나는지 확인 (if)
            if left < 0 or right >= N:
                # 범위를 벗어나면 이 회차의 뒤집기는 중지
                break
            
            # 마주보는 두 돌의 색이 같은지 확인 (elif / if)
            if s[left] == s[right]:
                # 색이 같으면 둘 다 뒤집기 (0 -> 1, 1 -> 0)
                if s[left] == 0:
                    s[left] = 1
                    s[right] = 1
                elif s[left] == 1:
                    s[left] = 0
                    s[right] = 0
            else:
                # 색이 다르면 그대로 둔다 (아무것도 하지 않음)
                pass

    # 결과 출력
    print(f"#{tc}", *s)