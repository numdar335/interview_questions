// task description: https://leetcode.com/problems/missing-number/
class Solution {
public:
  int missingNumber(vector<int>& nums) {
    short n = nums.size();
    sort(nums.begin(),nums.end());
    if (nums[0]) return 0;
    else if (n == 1 & !nums[0]) return 1;
    for (short i = 1; i < n; ++i)
      if (nums[i]-nums[i-1] == 2) return nums[i]-1;
    return n;
  }
};
