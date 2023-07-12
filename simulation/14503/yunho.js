const path = require('path');
const fs = require('fs');

const rawInputs = fs
  //	.readFileSync('/dev/stdin')
  .readFileSync(path.resolve(__dirname, '../today/1.txt'))
  .toString()
  .trim()
  .split('\n')
  .map((e) => e.split(' ').map((v) => +v));

// 북동남서
const dr = [-1, 0, 1, 0];
const dc = [0, 1, 0, -1];

const solution = (rawInputs) => {
  const [[r, c], [x, y, d], ...arr] = rawInputs;
  let answer = 0;

  // 청소 : 2

  let breakAll = false;
  const searchDfs = (cr, cc, cd) => {
    if (breakAll) return;

    if (arr[cr][cc] === 0) {
      answer++;
      arr[cr][cc] = 2;
    }

    let flag = true; // 주변 4칸 중 청소되지 않은 빈 칸이 있니 ? true: false
    for (let i = 0; i < 4; i++) {
      const nd = (cd + 3 - i) % 4; // 반 시계로 돌기
      const nr = cr + dr[nd];
      const nc = cc + dc[nd];
      if (nr < 0 || nr >= r || nc < 0 || nc >= c) continue;

      if (arr[nr][nc] === 0) {
        flag = false;
        searchDfs(nr, nc, nd);
      }
    }

    // 주변에 빈 칸이 없는 경우
    if (flag) {
      // 반대 방향
      const nd = cd + 2 < 4 ? cd + 2 : cd - 2;
      const nr = cr + dr[nd];
      const nc = cc + dc[nd];

      if (nr < 0 || nr >= r || nc < 0 || nc >= c) return;
      if (arr[nr][nc] === 1) {
        breakAll = true;
        return;
      }

      searchDfs(nr, nc, cd);
    }
  };

  searchDfs(x, y, d);

  return answer;
};

console.log(solution(rawInputs));

module.exports = { solution };
