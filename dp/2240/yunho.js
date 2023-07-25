// https://wooono.tistory.com/643 참고
const path = require('path');
const fs = require('fs');

const rawInputs = fs
  //	.readFileSync('/dev/stdin')
  .readFileSync(path.resolve(__dirname, '../today/1.txt'))
  .toString()
  .trim()
  .split('\n');

const solution = (rawInputs) => {
  const [t, w] = rawInputs[0].split(' ').map((v) => +v);
  const arr = rawInputs.slice(1).map((v) => +v);

  const dp = Array.from({ length: t + 1 }, () => Array.from({ length: w + 1 }, () => 0));
  // dp[r][c]: r초까지 c번 움직였을 때 최대

  const isSecond = (i) => i % 2 === 1;
  // j: 이동횟수
  // j : 짝수 -> 1나무
  // j : 홀수 -> 2나무
  for (let i = 1; i <= t; i++) {
    for (let j = 0; j <= w; j++) {
      // 이동안할 때 초기화
      if (j === 0) {
        if (arr[i - 1] === 1) {
          dp[i][j] = dp[i - 1][j] + 1;
        } else {
          dp[i][j] = dp[i - 1][j];
        }
        continue;
      }
      // dp[i - 1][j - 1] => 이동 안 함 && 이전 초
      // dp[i - 1][j] => 이동 함 && 이전 초
      // 이동했는데 2나무
      if (isSecond(j) && arr[i - 1] === 2) {
        dp[i][j] = Math.max(dp[i - 1][j - 1], dp[i - 1][j]) + 1;

        continue;
      }
      // 이동했는데 1나무
      if (!isSecond(j) && arr[i - 1] === 1) {
        dp[i][j] = Math.max(dp[i - 1][j - 1], dp[i - 1][j]) + 1;

        continue;
      }
      // 둘다 아님
      dp[i][j] = Math.max(dp[i - 1][j - 1], dp[i - 1][j]);
    }
  }

  // return dp[t][w]; -> 그냥 마지막꺼하면 이동하지 않았을 때 최대가 되는 예외케이스에서 걸림
  const answer = Math.max(...dp[t]);
  return answer;
};

console.log(solution(rawInputs));

module.exports = { solution };
