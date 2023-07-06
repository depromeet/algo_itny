const path = require('path');
const fs = require('fs');

const rawInputs = fs
  //	.readFileSync('/dev/stdin')
  .readFileSync(path.resolve(__dirname, '../today/1.txt'))
  .toString()
  .trim()
  .split('\n');

// L ->  idx - 1
// R -> idx + 1
const drMap = [
  (r, c) => [r, c + 1], //오른쪽
  (r, c) => [r + 1, c], //아래
  (r, c) => [r, c - 1], //왼쪽
  (r, c) => [r - 1, c], //위
];

const turnDirection = (drIdx, dr) => {
  if (dr === 'L') {
    return drIdx - 1 < 0 ? 3 : drIdx - 1;
  } else {
    return drIdx + 1 > 3 ? 0 : drIdx + 1;
  }
};

const solution = (rawInputs) => {
  const n = Number(rawInputs[0]);
  const k = Number(rawInputs[1]);

  const apples = rawInputs.slice(2, k + 2).map((e) => e.split(' ').map((v) => +v));

  const directions = rawInputs
    .slice(k + 3)
    .map((e) => e.split(' '))
    .reduce((acc, [time, dr]) => {
      acc[time] = dr;
      return acc;
    }, {});

  const board = Array.from({ length: n }, () => Array.from({ length: n }, () => 0));
  // 0: 빔, 1: 방문, -1: 사과
  apples.forEach(([r, c]) => {
    board[r - 1][c - 1] = -1; // 사과
  });

  const dequeue = [[0, 0]];
  board[0][0] = 1; // 뱀의 처음 위치

  let time = 0;
  let drIdx = 0;

  while (true) {
    // 방향 최신화

    const [nr, nc] = drMap[drIdx](...dequeue[0]); // 머리 방향 이동
    time++;

    // 범위 벗어남 || 자기 몸 만남
    if (nr < 0 || nr >= n || nc < 0 || nc >= n || board[nr][nc] === 1) break;

    // 사과있음
    if (board[nr][nc] === -1) {
      dequeue.unshift([nr, nc]);
    } else {
      // 사과 못 먹으면 꼬리 자르기
      dequeue.unshift([nr, nc]);
      const [tr, tc] = dequeue.pop();
      board[tr][tc] = 0;
    }

    board[nr][nc] = 1; // 사과제거 및 방문처리

    if (directions[time] !== undefined) {
      drIdx = turnDirection(drIdx, directions[time]);
    }
  }

  return time;
};

console.log(solution(rawInputs));

module.exports = { solution };
