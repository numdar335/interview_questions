//task description: https://leetcode.com/problems/first-unique-character-in-a-string/
class Solution {
public:
  int firstUniqChar(string s) {
    vector<int> A(26);
    fill(A.begin(),A.end(),0);
    int n = s.size();
    for (int i = 1; i <= n; ++i) ++A[s.at(i-1)-97];
    for (int i = 1; i <= n; ++i)
     if (A[s.at(i-1)-97] == 1) return i-1;
    return -1;
  }
};
