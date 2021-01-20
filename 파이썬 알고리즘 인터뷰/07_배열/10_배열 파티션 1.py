# LeetCode 561. Array Partition I
# n개의 페어를 이용한 min(a, b)의 합으로 만들 수 있는 가장 큰 수를 출력하라

class Solution:
    def arrayPairSum(self, nums):
        nums.sort(reverse=True) # 내림차순으로 정렬
        n = len(nums)
        result = 0
        for i in range(0, n, 2): # 두 칸씩 건너뛰기
            result += min(nums[i], nums[i+1])
        return result


if __name__ == "__main__":
    # example 데이터
    input_data = [1,4,3,2]
    
    solution = Solution()

    # 알고리즘 테스트
    answer = solution.arrayPairSum(input_data)
    print(answer)