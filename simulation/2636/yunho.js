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

const solution = (rawInputs) => {
  const [[n, m], ...arr] = rawInputs;

  const isDividedBy = () => {
    const visited = Array.from({ length: n }, () => Array.from({ length: m }, () => false));
    let cheese = 0;

    // hole = -10
    const checkHole = (r, c) => {
      const stack = [[r, c]];
      const temp = [[r, c]];
      let isEnd = false;
      outer: while (stack.length) {
        const [cr, cc] = stack.pop();
        inner: for (let i = 0; i < 4; i++) {
          const nr = dr[i] + cr;
          const nc = dc[i] + cc;

          if (nr < 0 || nr >= n || nc < 0 || nc >= m) {
            isEnd = true;
            continue;
          }

          if (!visited[nr][nc] && arr[nr][nc] === 0) {
            visited[nr][nc] = true;
            arr[nr][nc] = -10;
            stack.push([nr, nc]);
            temp.push([nr, nc]);
          }
        }
      }
      if (isEnd) {
        temp.forEach(([r, c]) => {
          arr[r][c] = 0;
        });
      }
    };

    for (let r = 0; r < n; r++) {
      for (let c = 0; c < m; c++) {
        if (arr[r][c] === 0) {
          checkHole(r, c);
          continue;
        }
        if (arr[r][c] === 1) {
          cheese++;
        }
      }
    }
    return cheese;
  };

  const melt = () => {
    for (let r = 0; r < n; r++) {
      for (let c = 0; c < m; c++) {
        if (arr[r][c] <= 0) continue;

        let side = 0;
        for (let i = 0; i < 4; i++) {
          const nr = dr[i] + r;
          const nc = dc[i] + c;
          if (nr < 0 || nr >= n || nc < 0 || nc >= m) continue;
          if (arr[nr][nc] === 0) {
            side = 2;
          }
        }
        arr[r][c] -= side;
        // 같은 시간에 옆 치즈 영향 방지
        if (arr[r][c] <= 0) {
          arr[r][c] = -1;
        }
      }
    }

    // 다음 시간에 치즈 녹일 수 있게 -1 => 공기로 바꾸기
    for (let r = 0; r < n; r++) {
      for (let c = 0; c < m; c++) {
        if (arr[r][c] === -1) {
          arr[r][c] = 0;
        }
        if (arr[r][c] === -10) {
          arr[r][c] = 0;
        }
      }
    }
  };

  let answer = 0;
  let time = 0;
  while (true) {
    const count = isDividedBy();
    if (count === 0) {
      break;
    } else {
      answer = count;
    }

    melt();
    time++;
  }

  return [time, answer].join('\n');
};

console.log(solution(rawInputs));

module.exports = { solution };
