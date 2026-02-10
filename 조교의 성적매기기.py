# 테스트 케이스 받기
T = int(input())
for tc in range(1, T+1):
    # 학생수와 알고 싶은 학생 번호
    N, K = map(int, input().split())
    grad = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    # 중 , 기, 과 성적 리스트 만들기
    arr = [list(map(int, input().split()))for _ in range(N)]
    total_cnt = []
    # 행 우선 순회 하며 카운트
    for i in range(N):
        if i == K:# 만약 k번째 학생이라면
            # k 학생 점수를 따로 부여
            k_cnt = 0
            for k_j in range(3):
                if k_j == 0:
                    k_cnt += (35 * arr[j][0])/100
                if k_j == 1:
                    k_cnt += (45 * arr[j][0])/100
                if k_j == 2:
                    k_cnt += (20 * arr[j][0])/100
        cnt = 0
        for j in range(3):
            if j == 0:
                cnt += (35 * arr[j][0])/100
            if j == 1:
                cnt += (45 * arr[j][0])/100
            if j == 2:
                cnt += (20 * arr[j][0])/100
    print(cnt)
    # #학생들의 종합 점수를 빈리스트에 넣기
    # total_cnt.append(cnt)
    # # 총점 기준으로 오름차순 정리
    # total_cnt.sort(reverse=True)
    # print(total_cnt)
    # 전체 점수 중에서 k 학생 점수의 순서를 찾기
#     for num in range(N):
#         if total_cnt[num] == k_cnt: # 만약에 num번째 점수와 k학생의 점수가 같다면
#             answer = grad[num//(N/10)-1]
# print(f'#{tc} {answer}')