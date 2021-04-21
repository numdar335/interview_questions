#task description: https://leetcode.com/problems/letter-combinations-of-a-phone-number/submissions/
class Solution(object):
  def letterCombinations(self,digits):
    if not digits: return digits
    A = [['a','b','c',''],['d','e','f',''],['g','h','i',''],['j','k','l',''],['m','n','o',''],['p','q','r','s'],['t','u','v',''],['w','x','y','z'],['','','','']]
    B = [3,3,3,3,3,4,3,4,1]
    C = [int(digits[0])-2,8,8,8]
    D = []
    for i in range(0,B[C[0]]):
      for x in range(1,len(digits)): C[x] = int(digits[x])-2
      for j in range (0,B[C[1]]):
        for k in range (0,B[C[2]]):
          for l in range (0,B[C[3]]):
            D.append(A[C[0]][i]+A[C[1]][j]+A[C[2]][k]+A[C[3]][l])
    return D
