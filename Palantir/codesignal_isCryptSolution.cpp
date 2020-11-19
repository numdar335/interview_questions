//task description: https://app.codesignal.com/interview-practice/task/yM4uWYeQTHzYewW9H/description
bool isCryptSolution(vector<string> crypt, vector<vector<char>> solution) {
  short A[3], m, c, n = solution.size();
  for (short i = 1; i <= 3; ++i) {
    A[i-1] = 0;
    m = crypt[i-1].size();
    c = 1;
    for (short j = m; j >= 1; --j)
      for (short k = 1; k <= n; ++k)
        if (crypt[i-1].at(j-1) == solution[k-1][0]) {
          A[i-1] += c*(solution[k-1][1]-48);
          c *= 10;
          if (!(solution[k-1][1]-48))
            if (j == 1 && m > 1 ) return false;
          k = n+1;
        }
  }
  if (A[0]+A[1] == A[2]) return true;
  return false;
}
