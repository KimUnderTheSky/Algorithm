# 배열을 입력받아 합으로 0을 만들 수 있는 3개의 엘리먼트를 출력하라
# 일반적인 브루트 포스로 계산하면 O(n^3)의 시간복잡도가 발생한다.
# 풀이(투포인터)
# 1. 배열 0부터 조회
# 2. 투포인터로 i값과 같으면 할당
nums = [-1,0,1,2,-1,-4]

def threeSum(nums):
    entry = [] # 3개의 엘리먼트 튜플을 담은 리스트 
    nums.sort()
    for i in range(len(nums)): # 배열 조회
        j = i+1
        k = len(nums) - 1
        while j < k: # 투포인터 
            print("인덱스값은: ", i, j, k)
            if (nums[i] - (nums[j] + nums[k])) == 0:
                entry.append((nums[i],nums[j],nums[k]))
            
            elif (nums[i] - (nums[j] + nums[k])) < 0:
                j += 1
            else:
                k -= 1
    return entry

solution = threeSum(nums)
print(solution)