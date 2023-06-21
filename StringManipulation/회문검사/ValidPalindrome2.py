import re


def isPalindrome(s: str) -> bool:
    s = s.lower()
    # 정규식으로 불필요한 문자 필터링
    s = re.sub('[^a-z0-9]','',s)

    return s == s[::-1] # 파이썬 슬라이싱으로 뒤집기
A = "race car"

answer = isPalindrome(A)

if answer:
    print("회문입니다.")
else:
    print("회문이 아닙니다.")