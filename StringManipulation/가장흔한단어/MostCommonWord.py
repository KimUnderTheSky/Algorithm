# 금지된 단어 제외한 가장 흔하게 등장하는 단어 출력, 대소문자 구분 X, 구두점 무시
# from ast import List
from typing import List
import collections
import re


paragraph = "Bob hit a ball, the hit BALL flew far after it was hit"
banned = ["hit"]

# 공백을 기준으로 스플릿, 전처리
# banned 단어 제외
# 최빈 단어 찾기 딕셔너리 사용

def mostCommonWord(paragraph: str, banned: List[str]) -> str: # 함수 매개변수의 타입 어노테이션, 매개변수의 타입을 지정한다. -> 반환값도 str임
    words = [word for word in re.sub(r'[^\w]',' ', paragraph) # 문장에서 단어 단위로 잘라서 전처리하여 word리스트 생성 후 list comprehension, ^ == not, \w == 단어 즉 단어가 아닌 문자는 공백 " "으로 대체 
             .lower().split if word not in banned] # 리스트 컴프리헨션의 조건절, banned에 포함되지 않은 단어만을 대상으로 한다.
    
    counts = collections.Counter(words)
    return counts.most_common(1)[0][0]
        
result = mostCommonWord(paragraph,banned)
print(result)

## 문제 해결중