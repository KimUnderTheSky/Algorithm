# 시간 측정
import time
from typing import List
start = time.time()  # 시작 시간 저장


# 덧셈하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스를 리턴하라.

# 풀이
# in을 이용한 탐색
# 모든 조합을 비교하지 않고 정답, 즉 타겟에서 첫번째 값을 뺀 값 target-n이 존재하는지 탐색문제로 변경

nums = [2,3,6,7,11,15]
target = 9


def twoSum(nums: List[int], target: int) -> List[int]:
    for i, n in enumerate(nums):
        # 정답 찾기
        complement = target - n
        # 답이 nums[i] 다음의 값들 중 존재하면 인덱스 반환
        if complement in nums[i+1:]:
            return [nums.index(n), nums[i+1:].index(complement)+(i+1)]
        
target_indices = twoSum(nums, target)
print(target_indices)

 
# 시간 측정
print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간