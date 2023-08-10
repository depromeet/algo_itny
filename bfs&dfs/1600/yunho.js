const path = require('path');
const fs = require('fs');

const rawInputs = fs
  //	.readFileSync('/dev/stdin')
  .readFileSync(path.resolve(__dirname, '../today/1.txt'))
  .toString()
  .trim()
  .split('\n')
  .map((e) => e.split(' ').map((v) => +v));

const dr = [1, -1, 0, 0];
const dc = [0, 0, 1, -1];
const hr = [1, 1, 2, 2, -1, -1, -2, -2];
const hc = [-2, 2, -1, 1, -2, 2, -1, 1];

const solution = (rawInputs) => {
  const [[k], [w, h], ...arr] = rawInputs;
  let answer = 0;

  const visited = Array.from({ length: h }, () =>
    Array.from({ length: w }, () => Array.from({ length: k }, () => false))
  );

  const isOverRange = (r, c) => r < 0 || r >= h || c < 0 || c >= w;

  const isWall = (r, c) => arr[r][c] === 1;

  const bfs = () => {
    const queue = [];
    queue.push([0, 0, 0, 0]); // r c k count
    visited[0][0][0] = true;
    let idx = 0;
    while (queue.length > idx) {
      const [cr, cc, ck, count] = queue[idx];
      if (cr === h - 1 && cc === w - 1) {
        answer = count;
        return;
      }

      // 말이동
      if (ck < k) {
        for (let i = 0; i < 8; i++) {
          const nr = cr + hr[i];
          const nc = cc + hc[i];
          if (isOverRange(nr, nc)) continue;
          if (isWall(nr, nc)) continue;
          if (visited[nr][nc][ck + 1]) continue;
          visited[nr][nc][ck + 1] = true;
          queue.push([nr, nc, ck + 1, count + 1]);
        }
      }

      // 일반 이동
      for (let i = 0; i < 4; i++) {
        const nr = cr + dr[i];
        const nc = cc + dc[i];
        if (isOverRange(nr, nc)) continue;
        if (isWall(nr, nc)) continue;
        if (visited[nr][nc][ck]) continue;
        visited[nr][nc][ck] = true;
        queue.push([nr, nc, ck, count + 1]);
      }

      idx++;
    }
    answer = -1;
  };
  bfs();

  return answer;
};

console.log(solution(rawInputs));

module.exports = { solution };
