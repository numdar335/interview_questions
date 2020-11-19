#task description: https://leetcode.com/problems/spiral-matrix/
class Solution:
  def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
    n, k, i, j = 0, 0, 1, 1
    x, y = len(matrix), len(matrix[0])
    if y > 1: r, d = True, False
    else: r, d = False, True
    l, u = False, False
    A = []
    A.append(matrix[0][0])
    for k in range (1,x*y):
      if r:
        j += 1
        if j == y-n: r, d = False, True
      elif d:
        i += 1
        if i == x-n: d, l = False, True
      elif l:
        j -= 1
        if j == 1+n: l, u, sy = False, True, True
      else:
        if sy:
          sy = False
          n += 1
        i -= 1
        if i == 1+n: u, r = False, True
      A.append(matrix[i-1][j-1])
    return A
