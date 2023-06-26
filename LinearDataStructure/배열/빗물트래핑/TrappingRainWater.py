# 높이를 입력받아 비 온 후 얼마나 많은 물이 쌓일 수 있는지 계산하라

# 풀이(투포인터)
# 1. 좌우측 투포인터를 사용하여 최대 높이를 향해 이동
# 2. 투 포인터 각각의 최댓값을 보관하여 이동하는 포인터 인덱스의 높이와 비교, 최대값과의 차이가 빗물이 고인 높이

from typing import List


height = [0,1,0,2,1,0,1,3,2,1,2,1]

def trapping_rain(height: List[int]) -> int:
    if not height:
        return 0
    
    volume = 0
    left, right = 0, len(height) - 1 # 좌우측 인덱스
    left_max, right_max = height[left], height[right] # 좌우 높이       

    while left < right:
        left_max, right_max = max(height[left], left_max), max(height[right],right_max) 
        # 왼쪽 포인터의 최댓값(left_max), 왼쪽 포인터의 그 당시 높이(height[left])를 비교하여 큰 값 할당, 우측도 동일

        #더 높은 쪽을 향해 투 포인터 이동
        if left_max <= right_max:
            volume += left_max - height[left]
            left += 1
        else:
            volume += right_max - height[right]
            right -= 1

    return volume

rain_count = trapping_rain(height)
print(rain_count)