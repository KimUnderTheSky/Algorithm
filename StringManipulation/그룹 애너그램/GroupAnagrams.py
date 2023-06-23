# 문자열 배열을 받아 애너그램 단위로 그룹핑하라

#풀이
# 1. 단어의 문자열을 정렬
# 2. 딕셔너리에 추가

import collections
from typing import List


words = ["eat","tea","tan", "ate","nat","bat"] 
sorted_words = []

def groupAnagrams(strs: List[str]) -> List[List[str]]: # 리스트 입력, 리스트 안에 리스트가 들어있는 자료형 출력
    anagrams = collections.defaultdict(list)

        # List
    for word in strs:
        # 정렬하여 리스트에 추가
        anagrams[''.join(sorted(word))].append(word) 
        # anagram은 딕셔너리. 정렬된 word를 키로 하여 word를 삽입, sorted메서드 사용 시 문자열을 리스트로 반환하기 때문에 ''문자열에 join()시키면서 다시 문자열로 결합할 수 있다.
        # sorted와 다르게 .sort()메서드는 제자리 정렬을 함으로 None을 반환
    return list(anagrams.values())

anagrams = groupAnagrams(words)
print(anagrams)
# 풀이중