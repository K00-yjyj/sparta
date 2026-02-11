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
        cnt = 0
        for j in range(3):
            if j == 0:
                cnt += (35 * arr[i][0])/100
            if j == 1:
                cnt += (45 * arr[i][1])/100
            if j == 2:
                cnt += (20 * arr[i][2])/100
        #학생들의 종합 점수를 빈리스트에 넣기
        total_cnt.append(cnt)
        if i == K-1:# 만약 k번째 학생이라면
            k_cnt = 0
            for k_j in range(3):
                if k_j == 0:
                    k_cnt += (35 * arr[i][0])/100
                if k_j == 1:
                    k_cnt += (45 * arr[i][1])/100
                if k_j == 2:
                    k_cnt += (20 * arr[i][2])/100
    # 총점 기준으로 오름차순 정리
    total_cnt.sort(reverse=True)
    # k 학생 총점 등수 인덱스 값 구하기
    num = total_cnt.index(k_cnt)
    # 학생 등수를 등급별 들어갈 인원수로 나누고 해당하는 등급 부여
    answer = grad[num//(N//10)] 
    print(f'#{tc} {answer}')   

   
