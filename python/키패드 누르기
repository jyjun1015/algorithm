def solution(numbers, hand):

    answer = ''
    key_dict = {'1':[0,0],
          '2':[0,1],
          '3':[0,2],
          '4':[1,0],
          '5':[1,1],
          '6':[1,2],
          '7':[2,0],
          '8':[2,1],
          '9':[2,2],
          '11':[3,0],
          '0':[3,1],
          '12':[3,2]}

    def middle_hand(num, l_pos, r_pos):
        a, b = key_dict[str(l_pos)]
        c, d = key_dict[str(r_pos)]
        x, y = key_dict[str(num)]
        dist_L = abs(a-x) + abs(b-y)
        dist_R = abs(c-x) + abs(d-y)
        if dist_L == dist_R:
            if hand == 'right':
                return 'R'
            else :
                return 'L'
        elif dist_L < dist_R:
            return 'L'
        else :
            return 'R'
    
    # 초기 값
    l_pos = 11
    r_pos = 12
    
    for num in numbers:
        if num in [1,4,7]:
            answer += 'L'
            l_pos = num
        elif num in [3,6,9]:
            answer += 'R'
            r_pos = num 
        else : 
            if middle_hand(num, l_pos, r_pos) == 'L':
                answer += 'L'
                l_pos = num
            else :
                answer += 'R'
                r_pos = num 
    return answer
