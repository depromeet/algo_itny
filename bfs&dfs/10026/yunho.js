const path = require('path');
const fs = require('fs');

const rawInputs = fs
  // .readFileSync('/dev/stdin')
  .readFileSync(path.resolve(__dirname, '../10026-g5-적록색약/1.txt'))
  .toString()
  .trim()
  .split('\n');

const dr = [1, -1, 0, 0];
const dc = [0, 0, 1, -1];

// // 틀렸음
// const solution = (rawInputs) => {
//   const [N, ...arr] = rawInputs;
//   const n = Number(N);
//   const answer = [0, 0]; // 0: 적록색약 아닌 사람, 1: 적록색약인 사람

//   const visitedRGB = Array.from({ length: n }, () => Array(n).fill(false));
//   const visitedRG = Array.from({ length: n }, () => Array(n).fill(false));

//   // 적록색약 아닌 사람
//   const dfsRGB = (target, r, c) => {
//     visitedRGB[r][c] = true;
//     for (let i = 0; i < 4; i++) {
//       const nr = dr[i] + r;
//       const nc = dc[i] + c;
//       if (0 > nr || n <= nr || 0 > nc || n <= nc) continue;
//       if (arr[nr][nc] !== target) continue;
//       if (visitedRGB[nr][nc]) continue;
//       // visitedRGB[nr][nc] = true;
//       dfsRGB(target, nr, nc);
//     }
//   };

//   // 적록색약인 사람
//   const dfsRG = (target, r, c) => {
//     visitedRG[r][c] = true;
//     for (let i = 0; i < 4; i++) {
//       const nr = dr[i] + r;
//       const nc = dc[i] + c;
//       if (0 > nr || n <= nr || 0 > nc || n <= nc) continue;
//       if (target === 'B') {
//         if (arr[nr][nc] !== 'B') continue;
//       }
//       if (target === 'R' || target === 'G') {
//         if (arr[nr][nc] === 'B') continue;
//       }
//       if (visitedRG[nr][nc]) continue;
//       // visitedRG[nr][nc] = true;
//       dfsRG(target, nr, nc);
//     }
//   };

//   const getResult = () => {
//     for (let r = 0; r < n; r++) {
//       for (let c = 0; c < n; c++) {
//         if (!visitedRGB[r][c]) {
//           // visitedRGB[r][c] = true;
//           dfsRGB(arr[r][c], r, c);
//           answer[0]++;
//         }
//         if (!visitedRG[r][c]) {
//           // visitedRG[r][c] = true;
//           dfsRG(arr[r][c], r, c);
//           answer[1]++;
//         }
//       }
//     }
//   };

//   getResult();

//   return answer.join(' ');
// };

// 맞음
const solution1 = (rawInputs) => {
  const [N, ...arr] = rawInputs.map((v) => v.split(''));
  const n = Number(N);
  const answer = [0, 0]; // 0: 적록색약 아닌 사람, 1: 적록색약인 사람

  let visited = Array.from({ length: n }, () => Array(n).fill(false));

  const dfs = (target, r, c) => {
    for (let i = 0; i < 4; i++) {
      const nr = dr[i] + r;
      const nc = dc[i] + c;
      if (0 > nr || n <= nr || 0 > nc || n <= nc) continue;
      if (arr[nr][nc] !== target) continue;
      if (visited[nr][nc]) continue;
      visited[nr][nc] = true;
      dfs(target, nr, nc);
    }
  };

  const getResult = (idx) => {
    for (let r = 0; r < n; r++) {
      for (let c = 0; c < n; c++) {
        if (!visited[r][c]) {
          visited[r][c] = true;
          dfs(arr[r][c], r, c);
          answer[idx]++;
        }
        // 적록색약인 사람용으로 변경하기
        if (idx === 0) {
          if (arr[r][c] === `G`) {
            arr[r][c] = `R`;
          }
        }
      }
    }
  };
  // 적록색약 아닌 사람
  getResult(0);

  // 방문배열 초기화하고 탐색
  visited = Array.from({ length: n }, () => Array(n).fill(false));

  // 적록색약인 사람
  getResult(1);

  return answer.join(' ');
};

console.log(solution1(rawInputs));
