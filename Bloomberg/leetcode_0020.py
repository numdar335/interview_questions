# task description: https://leetcode.com/problems/valid-parentheses/
class Solution(object):
  def isValid(self,s):
    helper = []
    for x in s:
      if x in ['(','{','[']: helper.append(x)
      elif helper:
        var = helper.pop()
        if (var != '(' and x == ')') or (var != '{' and x == '}') or (var != '[' and x == ']'): return False
      else: return False
    if not helper: return True
    return False
