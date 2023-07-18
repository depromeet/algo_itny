const path = require('path');
const fs = require('fs');

const rawInputs = fs
  //	.readFileSync('/dev/stdin')
  .readFileSync(path.resolve(__dirname, '../today/1.txt'))
  .toString()
  .trim()
  .split('\n')
  .map((e) => Number(e));

const solution = (rawInputs) => {
  const [n, ...arr] = rawInputs;

  const sorted = arr.sort((a, b) => a - b);

  const stack = [];

  const isOdd = (i) => i % 2 !== 0;

  let minus = 0;
  for (let i = 0; i < n; i++) {
    const target = sorted[i];
    // 음수
    if (target < 0) {
      minus++;
      if (isOdd(minus)) {
        stack.push(target);
      } else {
        const last = stack.pop();
        if (last === undefined) continue;
        stack.push(target * last);
      }

      continue;
    }

    // 0일 때
    if (target === 0) {
      const last = stack.pop();
      if (last === undefined) continue;
      if (last < 0) {
        // stack.push(0)
      } else {
        stack.push(last);
      }
      continue;
    }
  }

  let plus = 0;
  for (let i = n - 1; i >= 0; i--) {
    const target = sorted[i];
    // 양수
    if (target > 0) {
      plus++;
      if (target === 1) {
        plus--;
        stack.push(target);
        continue;
      }
      if (isOdd(plus)) {
        stack.push(target);
      } else {
        const last = stack.pop();
        if (last === undefined) continue;
        if (last === 1) {
          stack.push(last);
          stack.push(target);
        } else {
          stack.push(target * last);
        }
      }

      continue;
    }
  }

  const answer = stack.reduce((acc, cur) => acc + cur, 0);
  return answer;
};

console.log(solution(rawInputs));

module.exports = { solution };
