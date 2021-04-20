#task description: https://leetcode.com/problems/search-a-2d-matrix-ii/
class Solution(object):
  def searchMatrix(self,matrix,target):
    i, j = len(matrix)-1, 0
    while i >= 0 and j <= len(matrix[0])-1:
      if target < matrix[i][j]: i -= 1
      elif target > matrix[i][j]: j += 1
      else: return True
    return False
