const path = require('path');
const fs = require('fs');

const rawInputs = fs
  //	.readFileSync('/dev/stdin')
  .readFileSync(path.resolve(__dirname, '../today/1.txt'))
  .toString()
  .trim()
  .split('\n');

const dr = [1, -1, 0, 0];
const dc = [0, 0, 1, -1];

// bfs의 방문 배열 처리를 true, false로만 했는데 지금 문제처럼 시간 값 혹은 구하려는 최소 단위로 갱신해도 좋은 듯하다~

const solution = (w, h, arrs) => {
  const arr = arrs.map((v) => v.split(''));
  const visited = Array.from({ length: h }, () => Array.from({ length: w }, () => -1));
  const fireArr = Array.from({ length: h }, () => Array.from({ length: w }, () => -1));

  const cur = []; // 상근이 위치
  const fires = [];

  // 불 위치 초기화 및 상근이 위치 찾기
  for (let r = 0; r < h; r++) {
    for (let c = 0; c < w; c++) {
      if (arr[r][c] === '*') {
        fireArr[r][c] = 0;
        fires.push([r, c]);
      }
      if (arr[r][c] === '@') {
        visited[r][c] = 0;
        cur.push([r, c]);
      }
    }
  }

  let idx = 0;

  // 불이동
  while (fires.length > idx) {
    const [cr, cc] = fires[idx];

    // 불 처리
    for (let i = 0; i < 4; i++) {
      const nr = dr[i] + cr;
      const nc = dc[i] + cc;
      if (0 > nr || h <= nr || 0 > nc || w <= nc) continue;
      if (fireArr[nr][nc] > -1) continue;
      if (arr[nr][nc] === '#' || arr[nr][nc] === '*') continue;
      fireArr[nr][nc] = fireArr[cr][cc] + 1;
      fires.push([nr, nc]);
    }
    idx++;
  }

  idx = 0;
  // 상근이 이동
  let count = -1;
  outer: while (cur.length > idx) {
    const [cr, cc] = cur[idx];

    for (let i = 0; i < 4; i++) {
      const nr = dr[i] + cr;
      const nc = dc[i] + cc;
      if (0 > nr || h <= nr || 0 > nc || w <= nc) {
        count = visited[cr][cc] + 1;
        break outer;
      }
      if (visited[nr][nc] > -1) continue;
      if (arr[nr][nc] === '#' || arr[nr][nc] === '*') continue;
      // 가려는 곳에 불이 나있는 경우 12%..... 현재 시간(visited[r][c]) + 1 ≥ 불 시간 ⇒ 불이랑 동시에 도달하는 칸으로는 이동할 수 없다
      if (fireArr[nr][nc] !== -1 && visited[cr][cc] + 1 >= fireArr[nr][nc]) continue;
      visited[nr][nc] = visited[cr][cc] + 1;
      cur.push([nr, nc]);
    }
    idx++;
  }

  return count === -1 ? 'IMPOSSIBLE' : count;
};

const preSolution = (rawInputs) => {
  const t = rawInputs[0];
  let inputs = rawInputs[1];
  let rest = rawInputs.slice(2);
  const answer = [];
  for (let i = 0; i < t; i++) {
    const [w, h] = inputs.split(' ').map((v) => +v);
    const res = solution(w, h, rest.slice(0, h));
    answer.push(res);
    rest = rest.slice(h);
    inputs = rest[0];
    rest = rest.slice(1);
  }
  return answer.join('\n');
};

console.log(preSolution(rawInputs));

module.exports = { solution };
