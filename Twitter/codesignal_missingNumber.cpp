//task description: https://app.codesignal.com/interview-practice/task/PLCrGrJmBxQdj8QKX/description
int missingNumber(vector<int> arr) {
  sort(arr.begin(),arr.end());
  short n = arr.size();
  if (arr[0]) return 0;
  else if (n == 1 & !arr[0]) return 1;
  for (short i = 2; i <= arr.size(); ++i)
    if (arr[i-1]-arr[i-2] == 2) return arr[i-1]-1;
  return arr.size();
}
