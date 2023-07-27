const path = require('path');
const fs = require('fs');

const rawInputs = fs
  //	.readFileSync('/dev/stdin')
  .readFileSync(path.resolve(__dirname, '../today/1.txt'))
  .toString()
  .trim()
  .split('\n');

const solution = (rawInputs) => {
  const [inputs, ...arr] = rawInputs;
  const [n, r, q] = inputs.split(' ').map((v) => +v);
  const nodes = arr.slice(0, n - 1).map((e) => e.split(' ').map((v) => +v));
  const queries = arr.slice(n - 1).map((v) => +v);

  const tree = Array.from({ length: n + 1 }, () => []);
  const visited = Array.from({ length: n + 1 }, () => false);
  const dp = Array.from({ length: n + 1 }, () => 1); // i번째 노드의 서브트리

  for (const [u, v] of nodes) {
    tree[u].push(v);
    tree[v].push(u);
  }

  const dfs = (idx) => {
    visited[idx] = true;
    for (const next of tree[idx]) {
      if (visited[next]) continue;

      dfs(next);
      dp[idx] += dp[next];
    }
  };

  dfs(r);

  const answer = queries.map((v) => dp[v]);
  return answer.join('\n');
};

console.log(solution(rawInputs));

module.exports = { solution };
