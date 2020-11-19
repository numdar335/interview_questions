//task description: https://app.codesignal.com/interview-practice/task/CfknJzPmdbstXhsoJ/description
bool containsDuplicates(vector<int> a) {
  sort(a.begin(),a.end());
  int n = a.size();
  for (int i = 2; i <= n; ++i)
    if (a[i-1] == a[i-2]) return true;
  return false;
}
