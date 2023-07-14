const path = require('path');
const fs = require('fs');

const rawInputs = fs
  //	.readFileSync('/dev/stdin')
  .readFileSync(path.resolve(__dirname, '../today/1.txt'))
  .toString()
  .trim()
  .split('\n')
  .map((v) => v.split(''));

const R = 12;
const C = 6;
const dr = [1, -1, 0, 0];
const dc = [0, 0, 1, -1];

const solution = (rawInputs) => {
  let arr = rawInputs;

  const check = () => {
    let flag = false;
    const visited = Array.from({ length: R }, () => Array.from({ length: C }, () => false));
    for (let r = 0; r < R; r++) {
      for (let c = 0; c < C; c++) {
        if (arr[r][c] === '.') continue;
        const queue = [[r, c, arr[r][c]]];
        let idx = 0;
        while (queue.length > idx) {
          const [cr, cc, target] = queue[idx];

          for (let i = 0; i < 4; i++) {
            const nr = cr + dr[i];
            const nc = cc + dc[i];
            if (nr < 0 || nr >= R || nc < 0 || nc >= C) continue;
            if (visited[nr][nc]) continue;
            if (target !== arr[nr][nc]) continue;
            visited[nr][nc] = true;
            queue.push([nr, nc, target]);
          }
          idx++;
        }
        if (idx > 4) {
          for (const [cr, cc] of queue) {
            arr[cr][cc] = '.';
          }
          flag = true;
        }
      }
    }
    return flag;
  };

  const reArrange = () => {
    for (let c = 0; c < C; c++) {
      for (let r = R - 1; r >= 0; r--) {
        if (arr[r][c] !== '.') continue;
        let idx = r - 1;
        while (idx >= 0) {
          if (arr[idx][c] !== '.') {
            arr[r][c] = arr[idx][c];
            arr[idx][c] = '.';
            break;
          }
          idx--;
        }
      }
    }
  };
  let answer = 0;
  while (true) {
    const isBomb = check();
    if (!isBomb) break;
    answer++;
    reArrange();
  }

  return answer;
};

console.log(solution(rawInputs));

module.exports = { solution };
