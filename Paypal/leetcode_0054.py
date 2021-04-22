# task description: https://leetcode.com/problems/spiral-matrix/
class Solution:
  def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
    n, k, i, j, l, u, Arr, x, y = 0, 0, 1, 1, False, False, [], len(matrix), len(matrix[0])
    Arr.append(matrix[0][0])
    if y > 1: r, d = True, False
    else: r, d = False, True
    for k in range(1,x*y):
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
      Arr.append(matrix[i-1][j-1])
    return Arr
