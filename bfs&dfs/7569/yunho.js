const path = require('path');
const fs = require('fs');

const [input, ...arrs] = fs
  //	.readFileSync('/dev/stdin')
  .readFileSync(path.resolve(__dirname, '../today/1.txt'))
  .toString()
  .trim()
  .split('\n');

const direction = [
  [-1, 0, 0],
  [1, 0, 0],
  [0, 1, 0],
  [0, -1, 0],
  [0, 0, 1],
  [0, 0, -1],
];

const solution = (input, arr) => {
  const [M, N, H] = input.split(' ').map((v) => +v);
  let notRipen = 0;

  const box = arr
    .map((ele) => ele.split(' ').map((v) => +v))
    .reduce(
      (acc, cur, i) => {
        acc[Math.floor(i / N)].push(cur); // box만들기
        cur.forEach((tomato) => tomato === 0 && notRipen++); // 안 익은 토마토 개수 파악
        return acc;
      },
      [...Array(H)].map(() => [])
    );

  const visited = Array.from({ length: H }, () =>
    Array.from({ length: N }, () => Array.from({ length: M }, () => false))
  );

  let answer = 0;
  if (notRipen === 0) return answer;

  const queue = [];

  for (let h = 0; h < H; h++) {
    for (let c = 0; c < N; c++) {
      for (let r = 0; r < M; r++) {
        if (box[h][c][r] === 1) {
          queue.push([h, c, r, 0]);
        }
      }
    }
  }

  const bfs = () => {
    let idx = 0;
    while (queue.length !== idx) {
      const [h, c, r, acc] = queue[idx];
      for (const dr of direction) {
        const [x, y, z] = dr;
        const dx = x + r;
        const dy = y + c;
        const dz = z + h;
        if (dx < 0 || dy < 0 || dz < 0 || dx >= M || dy >= N || dz >= H) continue;
        if (box[dz][dy][dx] === 0 && !visited[dz][dy][dx]) {
          visited[dz][dy][dx] = true;
          box[dz][dy][dx] = 1;
          queue.push([dz, dy, dx, acc + 1]);
          notRipen--;
        }
      }
      idx++;
      answer = acc;
    }
  };
  bfs();

  if (notRipen) answer = -1;

  return answer;
};

console.log(solution(input, arrs));

module.exports = { solution };
