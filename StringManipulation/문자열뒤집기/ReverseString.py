from typing import List


A = input("문자열을 입력하세요: ")
def reverseString(s: List[str]): # s: List[str] 문자열을 리스트로 변환
    left, right = 0, len(s)-1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return s
A_reversed = reverseString(A)
print(A_reversed)

# 에러 : TypeError: 'str' object does not support item assignment -> 문자열 != 리스트, reverseString 파라미터 받을 때 List로 변환