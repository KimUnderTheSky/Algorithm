from ast import List


logs = ["dig1 8 1 5 1","let1 art can", "dig2 3 6","let2 own kit dig","let3 art zero"]

def reorderLogFiles(logs: List[str]):
    ordered_list_s = [] # 식별자가 문자인 리스트
    ordered_list_n = [] # 식별자가 숫자인 리스트
    for log in logs:
        if log.split()[1].isdigit(): # 따옴표 제외 하고 문자열 시작부분 [1]
            ordered_list_n.append(log)
        else:
            ordered_list_s.append(log)

    ordered_list_s.sort(key = lambda x: (x.split()[1:], x.split()[0])) #  sort메서드 내에 x가 key가 됨

    return ordered_list_s + ordered_list_n