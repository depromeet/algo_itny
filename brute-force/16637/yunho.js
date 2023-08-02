const path = require('path');
const fs = require('fs');

const rawInputs = fs
  //	.readFileSync('/dev/stdin')
  .readFileSync(path.resolve(__dirname, '../today/1.txt'))
  .toString()
  .trim()
  .split('\n');

const calc = {
  '+': (x, y) => Number(x) + Number(y),
  '-': (x, y) => Number(x) - Number(y),
  '*': (x, y) => Number(x) * Number(y),
};

const solution = (rawInputs) => {
  const n = Number(rawInputs[0]);
  const arr = rawInputs[1].split('');
  let answer = Number.MIN_SAFE_INTEGER;

  const isNumber = (x) => !isNaN(Number(x));

  const dfs = (idx, acc) => {
    if (idx >= n) {
      if (acc > answer) {
        answer = acc;
      }
      return;
    }

    if (isNumber(arr[idx])) {
      const cur = Number(arr[idx]);
      dfs(idx + 1, acc + cur);
      return;
    }
    // 연산 일 때
    const sign = arr[idx];

    // 바로 계산
    const next = arr[idx + 1];
    const res = calc[sign](acc, next);
    dfs(idx + 2, res);

    // 한 번 묶기
    if (idx + 3 <= n) {
      const x = arr[idx + 1];
      const nextSign = arr[idx + 2];
      const y = arr[idx + 3];
      const hideRes = calc[nextSign](x, y);
      const nextRes = calc[sign](acc, hideRes);
      dfs(idx + 4, nextRes);
    }
  };

  dfs(0, 0);

  return answer;
};

console.log(solution(rawInputs));

module.exports = { solution };
