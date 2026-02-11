T = int(input())
for tc in range(1,T+1):
    N = int(input()) # 테스트 케이스 번호
    # 성적 넣는 리스트
    grade_arr = list(map(int,input().split()))

    COUNTS = [0] * 101 # 0에서 100점까지 카운트 정렬하기 위한 값 지정

    for i in grade_arr:
        # 성적과 같은 인덱스에 위치한 원소 값을 COUNTS 함수에 넣기
        COUNTS[i] += 1
    
    #최빈값 구하는 방법
    max_grade =0
    reslut = 0
    # 점수의 최댓값 구하고 해당하는 인덱스 번호( 성적) 적음
    for grade in range(101):
        if max_grade <= COUNTS[grade]:
            max_grade = COUNTS[grade]
            reslut = grade
    print (f'{tc} {reslut}')
    