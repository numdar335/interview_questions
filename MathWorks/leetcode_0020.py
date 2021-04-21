#task description: https://leetcode.com/problems/valid-parentheses/
class Solution(object):
  def isValid(self,s):
    helper = []
    for i in s:
      if i in ['(','{','[']: helper.append(i)
      elif helper:
        temp = helper.pop()
        if (temp != '(' and i == ')') or (temp != '{' and i == '}') or (temp != '[' and i == ']'): return False
      else: return False
    if not helper: return True
    return False
