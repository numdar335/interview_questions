#task description: https://leetcode.com/problems/two-sum/
class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    A = []
    n = len(nums)
    for i in range(1,n+1):
      for j in range(i+1,n+1):
        if nums[i-1]+nums[j-1] == target:
          A.append(i-1)
          A.append(j-1)
          return A
