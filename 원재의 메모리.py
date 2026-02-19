T = int(input())

for tc in range(1, T + 1):
    # 공백 없는 문자열을 바로 list로 변환하여 한 글자씩 숫자로 만듭니다.
    arr = list(map(int, input())) 
    
    cnt = 0
    memory = 0  # 초기 상태 모든 bit 0이므로
    
    for i in arr:
        if i != memory:
            cnt += 1
            memory = i  # 현재 바뀐 값으로 뒤쪽이 다 바꿈
            
    print(f'#{tc} {cnt}')