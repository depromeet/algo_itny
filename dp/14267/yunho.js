const path = require('path');
const fs = require('fs');

const rawInputs = fs
  //	.readFileSync('/dev/stdin')
  .readFileSync(path.resolve(__dirname, '../today/1.txt'))
  .toString()
  .trim()
  .split('\n')
  .map((e) => e.split(' ').map((v) => +v));

const solution = (rawInputs) => {
  let [[n, m], superiors, ...compliments] = rawInputs;
  compliments = compliments.slice(0, m); // https://www.acmicpc.net/board/view/117771

  const tree = Array.from({ length: n + 1 }, () => []);
  const dp = Array.from({ length: n + 1 }, () => 0); // i번째 직원의 누적 칭찬

  for (let i = 1; i < n + 1; i++) {
    if (superiors[i - 1] === -1) continue;
    tree[superiors[i - 1]].push(i);
  }

  for (const [idx, w] of compliments) {
    // 중복 칭찬
    dp[idx] += w;
  }

  const dfs = (idx) => {
    for (const next of tree[idx]) {
      dp[next] += dp[idx];
      dfs(next);
    }
  };

  dfs(1);

  return dp.slice(1).join(' ');
};

console.log(solution(rawInputs));

module.exports = { solution };
