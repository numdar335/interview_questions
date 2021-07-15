class Solution(object):
  def letterCombinations(self,digits):
    if not digits: return digits
    n, A, B, C, D = len(digits), [['a','b','c',''],['d','e','f',''],['g','h','i',''],['j','k','l',''],['m','n','o',''],['p','q','r','s'],['t','u','v',''],['w','x','y','z'],['','','','']], [3,3,3,3,3,4,3,4,1], [int(digits[0])-2,8,8,8], []
    for i in range(B[C[0]]):
      for x in range(1,n): C[x] = int(digits[x])-2
      for j in range(B[C[1]]):
        for k in range(B[C[2]]):
          for l in range(B[C[3]]):
            D.append(A[C[0]][i]+A[C[1]][j]+A[C[2]][k]+A[C[3]][l])
    return D
