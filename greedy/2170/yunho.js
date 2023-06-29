const path = require('path');
const fs = require('fs');

const rawInputs = fs
  //	.readFileSync('/dev/stdin')
  .readFileSync(path.resolve(__dirname, '../today/1.txt'))
  .toString()
  .trim()
  .split('\n')
  .map((e) => e.split(' ').map((v) => +v));

// // 1트 ✅
// const solution = (rawInputs) => {
//   const [[n], ...arr] = rawInputs;
//   let acc = 0;

//   // 오름차순 정렬
//   const sorted = arr.sort((a, b) => (a[0] === b[0] ? a[1] - b[1] : a[0] - b[0]));

//   let [start, end] = sorted[0];

//   for (let i = 1; i < n; i++) {
//     const [cs, ce] = sorted[i];
//     // 오름차순 정렬 ->  start >= s

//     if (cs <= end) {
//       // 겹침
//       if (ce > end) {
//         // 범위가 늘어남
//         end = ce;
//       }
//       // 범위가 안 늘어남(포함되는 관계)
//     } else if (end < cs) {
//       // 안 겹침
//       acc += Math.abs(end - start);
//       start = cs;
//       end = ce;
//     }
//   }
//   acc += Math.abs(end - start);

//   return acc;
// };

// 2트 ✅
const solution = (rawInputs) => {
  const [[n], ...arr] = rawInputs;
  let acc = 0;

  // 오름차순 정렬
  const sorted = arr.sort((a, b) => (a[0] === b[0] ? a[1] - b[1] : a[0] - b[0]));

  let end = Number.MIN_SAFE_INTEGER;

  for (const [s, e] of sorted) {
    if (s >= end) {
      // 안 겹침
      acc += e - s;
      end = e; // 마지막 값 갱신
    } else if (s < end) {
      // 겹침
      if (e > end) {
        acc += e - end; // 안 겹치는 부분만큼 누적
        end = e;
      }
    }
  }

  return acc;
};

console.log(solution(rawInputs));

module.exports = { solution };
