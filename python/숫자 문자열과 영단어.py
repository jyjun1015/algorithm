def solution(s):
    s_dict = {'zero' : '0',
             'one' : '1',
             'two':'2',
             'three':'3',
             'four':'4',
             'five':'5',
             'six':'6',
             'seven':'7',
             'eight':'8',
             'nine':'9'}
    for s_key in s_dict:
        s = s.replace(s_key, s_dict[s_key])
    return int(s)
