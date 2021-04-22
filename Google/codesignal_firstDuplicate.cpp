//task description: https://app.codesignal.com/interview-practice/task/pMvymcahZ8dY4g75q/description
int firstDuplicate(vector<int> A) {
  vector<int> B(99999);
  fill(B.begin(),B.end(),0);
  B[A[0]] = 1;
  int n = A.size();
  for (int i = 1; i < n; ++i)
    if (++B[A[i]] > 1) return A[i];
  return -1;
}
