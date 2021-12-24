# task description: https://leetcode.com/problems/maximum-subarray/
class Solution(object):
  def findMaxCrossingSubArray(self,A,low,mid,high):
    leftSum, sum = -1e308, 0
    for i in reversed(range(low,mid+1)):
      sum += A[i]
      if sum > leftSum: leftSum, maxLeft = sum, i
    rightSum, sum = -1e308, 0
    for i in range(mid+1,high+1):
      sum += A[i]
      if sum > rightSum: rightSum, maxRight = sum, i
    return (maxLeft,maxRight,leftSum+rightSum)
  def findMaxSubArray(self,A,low,high):
    if high == low: return (low,high,A[low])
    else:
      mid = (low+high)//2
      (leftLow,leftHigh,leftSum) = self.findMaxSubArray(A,low,mid)
      (rightLow,rightHigh,rightSum) = self.findMaxSubArray(A,mid+1,high)
      (crossLow,crossHigh,crossSum) = self.findMaxCrossingSubArray(A,low,mid,high)
      if leftSum >= rightSum and leftSum >= crossSum: return (leftLow,leftHigh,leftSum)
      elif rightSum >= leftSum and rightSum >= crossSum: return (rightLow,rightHigh,rightSum)
      else: return (crossLow,crossHigh,crossSum)
  def maxSubArray(self,nums):
    (a,b,c) = self.findMaxSubArray(nums,0,len(nums)-1)
    return c
