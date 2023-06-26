# 높이를 입력받아 비 온 후 얼마나 많은 물이 쌓일 수 있는지 계산하라

# 풀이(스택)
# 1. 스택에 쌓아나간다.
# 2. 
from typing import List


height = [0,1,0,2,1,0,1,3,2,1,2,1]

def trapping_rain(height: List[int]) -> int:
    stack = []
    volume = 0

    for i in range(len(height)):
        # 변곡점을 만나는 경우
        while stack and height[i] > height[stack[-1]]:
            # 스택에서 꺼낸다.
            top = stack.pop()

            if not len(stack):
                break

            # 이전과의 차이만큼 물 높이 처리
            distance = i - stack[-1] - 1
            waters = min(height[i], height[stack[-1]])  - height[top]

            volume += distance * waters

        stack.append(i)
    return volume


rain_count = trapping_rain(height)
print(rain_count)