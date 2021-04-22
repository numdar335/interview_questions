# task description: https://leetcode.com/problems/pascals-triangle/
class Solution:
  def generate(self,numRows: int):
    A = []
    for i in range(numRows):
      B = []
      for j in range(i+1):
        if j not in [0,i]: B.append(A[i-1][j-1]+A[i-1][j])
        else: B.append(1)
      A.append(B)
    return A
