// task description: https://leetcode.com/problems/first-unique-character-in-a-string/
class Solution {
public:
  int firstUniqChar(string s) {
    vector<int> Arr(26);
    fill(Arr.begin(),Arr.end(),0);
    int i, n = s.size();
    for (i = 0; i < n; ++i) ++Arr[s.at(i)-97];
    for (i = 0; i < n; ++i)
     if (Arr[s.at(i)-97] == 1) return i;
    return -1;
  }
};
