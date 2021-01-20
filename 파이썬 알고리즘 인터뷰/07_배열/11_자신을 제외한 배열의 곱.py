# LeetCode 238. Product of Array Except Self
# 배열을 입력받아 output[i]가 자신을 제외한 나머지 모든 요소의 곱셈 결과가 되도록 출력하라
# 주의) 나눗셈을 하지 않고 O(n)에 풀이하라.

def productExceptSelf(nums):
    out = []
    p = 1
    for i in range(len(nums)):
        out.append(p)
        p = p * nums[i]

    p = 1
    for i in range(len(nums)-1, -1, -1):
        out[i] = out[i] * p
        p = p * nums[i]
    
    return out

nums = [1, 2, 3, 4]
print(productExceptSelf(nums))