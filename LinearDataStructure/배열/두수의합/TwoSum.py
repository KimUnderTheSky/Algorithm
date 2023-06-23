# 시간 측정
import time
from typing import List
start = time.time()  # 시작 시간 저장


# 덧셈하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스를 리턴하라.

# 풀이
# 이중배열, 더해서 9가 되면, 인덱스 반환
nums = [2,3,6,7,11,15]
target = 9

def TwoSum(A,target):
    target_indices = []
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if A[i] + A[j] == target:
                target_indices.append((i,j))
    return target_indices

target_indices = TwoSum(nums, target)
print(target_indices)

 
# 시간 측정
print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간