#task description: https://leetcode.com/problems/integer-to-english-words/
class Solution(object):
  def helper(self,a,b,c):
    s = ''
    flag = [False,False]
    a, b, c = int(a), int(b), int(c)
    Arr = [['One','Two','Three','Four','Five','Six','Seven','Eight','Nine'],['Eleven','Twelve','Thirteen','Fourteen','Fifteen','Sixteen','Seventeen','Eighteen','Nineteen'],['Ten','Twenty','Thirty','Forty','Fifty','Sixty','Seventy','Eighty','Ninety']]
    if a:
      s += Arr[0][a-1]+' Hundred'
      flag[0] = True
    if b != 1:
      if b:
        if flag[0]: s += ' '
        s += Arr[2][b-1]
        flag[1] = True
      if c:
        if flag[0] or flag[1]: s += ' '
        s += Arr[0][c-1]
    else:
      if flag[0]: s += ' '
      if c: s += Arr[1][c-1]
      else: s += Arr[2][0]
    return s
  def numberToWords(self,num):
    if not num: return 'Zero'
    outp = ''
    flag = [False,False,False]
    Arr = ['One','Two']
    s = str(num)
    n = len(s)
    for i in range(0,10-n): s = '0'+s
    if s[0] != '0':
      outp += Arr[int(s[0])-1]+' Billion'
      flag[0] = True
    t = self.helper(s[1],s[2],s[3])
    if t != '':
      if flag[0]: outp += ' '
      outp += t+' Million'
      flag[1] = True
    t = self.helper(s[4],s[5],s[6])
    if t != '':
      if flag[0] or flag[1]: outp += ' '
      outp += t+' Thousand'
      flag[2] = True
    t = self.helper(s[7],s[8],s[9])
    if t != '':
      if flag[0] or flag[1] or flag[2]: outp += ' '
      outp += t
    return outp
