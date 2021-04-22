#task description: https://leetcode.com/problems/two-sum/
class Solution:
  def twoSum(self,nums: List[int],target: int) -> List[int]:
    Arr = []
    n = len(nums)
    for i in range(n):
      for j in range(i+1,n):
        if nums[i]+nums[j] == target:
          Arr.append(i)
          Arr.append(j)
          return Arr
