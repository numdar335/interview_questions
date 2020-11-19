//task description: https://app.codesignal.com/interview-practice/task/pMvymcahZ8dY4g75q/description
int firstDuplicate(vector<int> a) {
  vector<int> b(99999);
  fill(b.begin(),b.end(),0);
  b[a[0]] = 1;
  int n = a.size();
  for (int i = 2; i <= n; ++i)
    if (++b[a[i-1]] > 1) return a[i-1];
  return -1;
}
