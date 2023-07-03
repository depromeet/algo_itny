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

// 1트: 메모리 초과, 시간초과
// 2트: ✅
// > 같은 time에 녹이는 도중 옆에 빙산에 영향가지 않게 처리하기`
// 1트에서는 같은 시간 해당 문제를 해결하기 위해 각 time마다 n * m크기의 배열을 매번 선언해서 메모리 초과가 발생
// → 2트에서는 현재 time에 0이하가 되었다면 -1로 처리해 바다로 인식하지 못하게하고, time에 해당하는 녹이기 작업이 끝났을 때 다시 -1을 바다로 변경해서 다음 time에 계산할 수 있도록 수정

const solution = (rawInputs) => {
  let [[n, m], ...arr] = rawInputs;

  const isDividedByTwo = () => {
    const visited = Array.from({ length: n }, () => Array.from({ length: m }, () => false));
    let ice = 0;

    const dfs = (r, c) => {
      const stack = [[r, c]];
      while (stack.length) {
        const [cr, cc] = stack.pop();
        for (let i = 0; i < 4; i++) {
          const nr = dr[i] + cr;
          const nc = dc[i] + cc;
          if (nr < 0 || nr >= n || nc < 0 || nc >= m) continue;
          if (!visited[nr][nc] && arr[nr][nc] !== 0) {
            visited[nr][nc] = true;
            stack.push([nr, nc]);
          }
        }
      }
    };

    for (let r = 0; r < n; r++) {
      for (let c = 0; c < m; c++) {
        if (arr[r][c] === 0) continue;
        if (visited[r][c]) continue;
        visited[r][c] = true;
        dfs(r, c);
        ice++;
      }
    }
    return ice;
  };

  let answer = 0;
  let time = 0;
  while (true) {
    const res = isDividedByTwo();
    // console.log('res', res);
    // console.log(arr.map((v) => v.join(' ')).join('\n'));

    if (res >= 2) {
      answer = time;
      break;
    }

    if (res === 0) {
      answer = 0;
      break;
    }

    // 얼음 녹이기
    for (let r = 0; r < n; r++) {
      for (let c = 0; c < m; c++) {
        if (arr[r][c] <= 0) continue;

        let sea = 0;
        for (let i = 0; i < 4; i++) {
          const nr = dr[i] + r;
          const nc = dc[i] + c;
          if (nr < 0 || nr >= n || nc < 0 || nc >= m) continue;
          if (arr[nr][nc] === 0) {
            sea++;
          }
        }
        arr[r][c] -= sea;
        // 같은 time에 녹이는 도중 옆에 빙산에 영향가지 않게 처리하기
        if (arr[r][c] <= 0) {
          arr[r][c] = -1;
        }
      }
    }

    // 다음 time에 빙산 녹일 수 있게 처리 수정
    for (let r = 0; r < n; r++) {
      for (let c = 0; c < m; c++) {
        if (arr[r][c] === -1) {
          arr[r][c] = 0;
        }
      }
    }

    time++;
  }

  return answer;
};

console.log(solution(rawInputs));

module.exports = { solution };
