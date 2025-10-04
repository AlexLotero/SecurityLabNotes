def isValid(s):
    # Write your code here
    str_list = list(set(s))
    print(str_list)
    first_char = str_list[0]
    first_char_cnt = s.count(first_char)
    correction = 0
    # visited = ''
    
    i = 1
    while i < len(str_list):
        difference = abs(s.count(str_list[i-1]) - s.count(str_list[i]))
        if difference != 0:
            # print('Adding to correction')
            correction += difference
        if correction > 1:
            return 'NO'
        i += 1
    return 'YES'




def isValid(s):
    # Write your code here
    str_list = list(set(s))
    print(str_list)
    first_char = str_list[0]
    first_char_cnt = s.count(first_char)
    correction = 0
    # visited = ''
    
    i = 1
    while i < len(str_list):
        difference = abs(s.count(str_list[i-1]) - s.count(str_list[i]))
        if difference != 0:
            # print('Adding to correction')
            try:
                diff_2 = abs(s.count(str_list[i-2]) - s.count(str_list[i]))
                correction += diff_2
            except Exception:
                pass
            correction += difference
        if correction > 1:
            return 'NO'
        i += 1
    return 'YES'




def isValid(s):
    # Write your code here
    str_list = list(set(s))
    # print(str_list)
    first_char = str_list[0]
    first_char_cnt = s.count(first_char)
    correction = 0
    # visited = ''
    for i in str_list:
        # print(first_char_cnt, s.count(i))
        # if i not in s:
        #     print('i not in s ', i)
        #     continue
        difference = abs(first_char_cnt - s.count(i))
        if difference != 0:
            # print('Adding to correction')
            correction += difference
        if correction > 1:
            return 'NO'
    return 'YES'