# 덱을 사용하여 해결

import collections
def isPalindrome(A):
    deque = collections.deque()
    for char in A:
        if char.isalnum(): # isalnum: 알파벳과 숫자로 이루어져있는가
            deque.append(char)
    while len(deque) > 1:
        if deque.popleft() != deque.pop(): # 덱의 전후단 요소 꺼내서 비교시 다르면 False반환
            return False
    return True
A = input("문자열 입력: ")
answer = isPalindrome(A)

if answer:
    print("회문입니다.")
else:
    print("회문이 아닙니다.")
