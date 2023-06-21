import re


def isPalindrome(s: str) -> bool:
    s = s.lower()
    # 정규식으로 불필요한 문자 필터링
    s = re.sub('[^a-z0-9]','',s)

    return s == s[::-1] # 파이썬 슬라이싱으로 뒤집기, 슬라이싱은 리스트의 reverse(), for while반복, 재귀 보다 더 빠른 무자열 처리 실행 시간을 가진다.
A = "race car"

answer = isPalindrome(A)

if answer:
    print("회문입니다.")
else:
    print("회문이 아닙니다.")