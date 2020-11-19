#task description: https://leetcode.com/problems/pascals-triangle/
class Solution:
  def generate(self, numRows: int):
    A = []
    for i in range(1,numRows+1):
      B = []
      for j in range(1,i+1):
        if j != i and j != 1: B.append(A[i-2][j-2]+A[i-2][j-1])
        else: B.append(1)
      A.append(B)
    return A
