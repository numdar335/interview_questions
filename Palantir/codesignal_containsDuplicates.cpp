// task description: https://app.codesignal.com/interview-practice/task/CfknJzPmdbstXhsoJ/description
bool containsDuplicates(vector<int> A) {
  sort(A.begin(),A.end());
  int n = A.size();
  for (int i = 1; i < n; ++i)
    if (A[i] == A[i-1]) return true;
  return false;
}
