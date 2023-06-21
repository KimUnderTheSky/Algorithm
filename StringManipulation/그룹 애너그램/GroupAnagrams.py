# 문자열 배열을 받아 애너그램 단위로 그룹핑하라

#풀이
# 1. 단어의 문자열을 정렬
# 2. 딕셔너리에 추가

import collections
from typing import List


words = ["eat","tea","tan", "ate","nat","bat"] 
sorted_words = []

def groupAnagrams(strs: List[str]) -> List[List[str]]: # 리스트 입력, 딕셔너리 출력
    anagrams = collections.defaultdict(list)

        # List
    for word in strs:
        # 정렬하여 딕셔너리에 추가
        anagrams[''.join(sorted(word))].append(word)
    return list(anagrams.values())


# 풀이중