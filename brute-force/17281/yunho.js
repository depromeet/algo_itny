const path = require('path');
const fs = require('fs');

const rawInputs = fs
  //	.readFileSync('/dev/stdin')
  .readFileSync(path.resolve(__dirname, '../today/1.txt'))
  .toString()
  .trim()
  .split('\n')
  .map((e) => e.split(' ').map((v) => +v));

// arr [0,0,0] (1,2,3)
const calc = [
  // 아웃
  (a, b, c) => [a, b, c, -1],
  // 1루타
  (a, b, c) => [1, a, b, c],
  // 2루타
  (a, b, c) => [0, 1, a, b + c],
  // 3루타
  (a, b, c) => [0, 0, 1, a + b + c],
  // 홈런
  (a, b, c) => [0, 0, 0, 1 + a + b + c],
];

const solution = (rawInputs) => {
  const [[n], ...arr] = rawInputs;
  let answer = Number.MIN_SAFE_INTEGER;

  // idx: 순서
  const order = Array.from({ length: 9 }, () => -1);
  // const order = [1, 2, 3, 0, 4, 5, 6, 7, 8];

  const getScore = () => {
    let score = 0;
    let hitter = 0;
    for (const innings of arr) {
      let a = 0;
      let b = 0;
      let c = 0;

      let out = 0;
      while (out < 3) {
        // 🚨 시간초과발생, 일반 if문으로 수정하기 https://www.acmicpc.net/board/view/113806
        // const [na, nb, nc, res] = calc[innings[order[hitter]]](a, b, c);
        const calc = innings[order[hitter]];
        if (calc === 0) {
          out++;
        } else if (calc === 1) {
          score += c;
          c = b;
          b = a;
          a = 1;
        } else if (calc === 2) {
          score += b + c;
          c = a;
          b = 1;
          a = 0;
        } else if (calc === 3) {
          score += a + b + c;
          c = 1;
          b = 0;
          a = 0;
        } else if (calc === 4) {
          score += a + b + c + 1;
          c = 0;
          b = 0;
          a = 0;
        }
        hitter = (hitter + 1) % 9;

        // hitter = (hitter + 1) % 9;
        // if (res === -1) {
        //   out++;
        //   continue;
        // }
        // score += res;
        // a = na;
        // b = nb;
        // c = nc;
      }
    }
    return score;
  };

  const dfs = (idx) => {
    if (idx === 9) {
      const score = getScore();
      answer = Math.max(score, answer);
      return;
    }
    for (let i = 0; i < 9; i++) {
      if (order[i] !== -1) continue;
      order[i] = idx;
      dfs(idx + 1);
      order[i] = -1;
    }
  };

  order[3] = 0;
  dfs(1); // 1번타자를 이미 배치해서 0이 아닌 1부터 시작해야함
  // getScore();

  return answer;
};

console.log(solution(rawInputs));

module.exports = { solution };
