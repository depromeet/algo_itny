const path = require('path');
const fs = require('fs');

const rawInputs = fs
  //	.readFileSync('/dev/stdin')
  .readFileSync(path.resolve(__dirname, '../today/1.txt'))
  .toString()
  .trim()
  .split('\n')
  .map((e) => e.split(' ').map((v) => +v));

const move = {
  [0]: (r, c, s) => [r - s, c],
  [1]: (r, c, s) => [r - s, c + s],
  [2]: (r, c, s) => [r, c + s],
  [3]: (r, c, s) => [r + s, c + s],
  [4]: (r, c, s) => [r + s, c],
  [5]: (r, c, s) => [r + s, c - s],
  [6]: (r, c, s) => [r, c - s],
  [7]: (r, c, s) => [r - s, c - s],
};

const dr = [-1, -1, 0, 1, 1, 1, 0, -1];
const dc = [0, 1, 1, 1, 0, -1, -1, -1];

const solution = (rawInputs) => {
  let [[n, m, k], ...arr] = rawInputs;
  let answer = 0;
  let table = Array.from({ length: n }, () => Array.from({ length: n }, () => []));

  // const isOverRange = (i) => (i + n) % n; 이거 왜 안돼애애애
  // ✅ s(속도)가 n보다 클 수 가 있음, 이 때 s를 n으로 나눈 나머지 만큼 이동해야함

  const moveFires = (table) => {
    const newTable = Array.from({ length: n }, () => Array.from({ length: n }, () => []));
    for (let r = 0; r < n; r++) {
      for (let c = 0; c < n; c++) {
        if (table[r][c].length === 0) continue;
        for (const fire of table[r][c]) {
          const [_, s, d] = fire;
          // const [nr, nc] = move[d](r, c, s).map(isOverRange);
          const nr = (r + dr[d] * (s % n) + n) % n;
          const nc = (c + dc[d] * (s % n) + n) % n;
          newTable[nr][nc].push(fire);
        }
      }
    }
    return newTable;
  };

  const afterMove = (table) => {
    const newTable = Array.from({ length: n }, () => Array.from({ length: n }, () => []));
    for (let r = 0; r < n; r++) {
      for (let c = 0; c < n; c++) {
        if (table[r][c].length < 2) {
          newTable[r][c] = table[r][c];
          continue;
        }
        const dr = [];
        let sm = 0;
        let ss = 0;
        for (const [m, s, d] of table[r][c]) {
          sm += m;
          ss += s;
          dr.push(d);
        }

        const allEven = dr.every((num) => num % 2 === 0);
        const allOdd = dr.every((num) => num % 2 !== 0);
        let moves = [];
        if (allEven || allOdd) {
          moves = [0, 2, 4, 6];
        } else {
          moves = [1, 3, 5, 7];
        }
        const nm = Math.floor(sm / 5);
        if (nm <= 0) continue;
        const ns = Math.floor(ss / table[r][c].length);
        for (const d of moves) {
          newTable[r][c].push([nm, ns, d]);
        }
      }
    }
    return newTable;
  };

  const init = () => {
    for (const [r, c, m, s, d] of arr) {
      table[r - 1][c - 1].push([m, s, d]);
    }
  };

  init();
  while (k > 0) {
    table = moveFires(table);
    table = afterMove(table);
    k--;
  }

  for (let r = 0; r < n; r++) {
    for (let c = 0; c < n; c++) {
      if (table[r][c].length > 0) {
        answer += table[r][c].reduce((acc, cur) => acc + cur[0], 0);
      }
    }
  }

  return answer;
};

console.log(solution(rawInputs));

module.exports = { solution };
