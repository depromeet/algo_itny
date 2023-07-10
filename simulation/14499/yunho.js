const path = require('path');
const fs = require('fs');

const rawInputs = fs
  //	.readFileSync('/dev/stdin')
  .readFileSync(path.resolve(__dirname, '../today/1.txt'))
  .toString()
  .trim()
  .split('\n')
  .map((e) => e.split(' ').map((v) => +v));

const drMap = {
  [1]: (r, c) => [r, c + 1], // 동
  [2]: (r, c) => [r, c - 1], // 서
  [3]: (r, c) => [r - 1, c], // 북
  [4]: (r, c) => [r + 1, c], // 남
};

const updateDice = {
  // 동
  [1]: (dice) => {
    const [a, b, c, d, e, f] = dice;
    return [c, b, f, a, e, d];
  },
  // 서
  [2]: (dice) => {
    const [a, b, c, d, e, f] = dice;
    return [d, b, a, f, e, c];
  },
  // 북
  [3]: (dice) => {
    const [a, b, c, d, e, f] = dice;
    return [e, a, c, d, f, b];
  },
  // 남
  [4]: (dice) => {
    const [a, b, c, d, e, f] = dice;
    return [b, f, c, d, a, e];
  },
};

const FLOOR = 0;
const CEIL = 5;

const solution = (rawInputs) => {
  const [r, c, x, y, k] = rawInputs[0];
  const arr = rawInputs.slice(1, r + 1);
  const orders = rawInputs.at(-1);
  const answer = [];

  let dice = Array.from({ length: 6 }, () => 0);
  const current = {
    r: x,
    c: y,
  };

  for (const order of orders) {
    const [nr, nc] = drMap[order](current.r, current.c);

    if (nr < 0 || nr >= r || nc < 0 || nc >= c) continue;
    dice = updateDice[order](dice);

    if (arr[nr][nc] === 0) {
      arr[nr][nc] = dice[FLOOR];
    } else {
      dice[FLOOR] = arr[nr][nc];
      arr[nr][nc] = 0;
    }

    current.r = nr;
    current.c = nc;

    answer.push(dice[CEIL]);
  }

  return answer.join('\n');
};

console.log(solution(rawInputs));

module.exports = { solution };
