const path = require('path');
const fs = require('fs');

const rawInputs = fs
  //	.readFileSync('/dev/stdin')
  .readFileSync(path.resolve(__dirname, '../today/1.txt'))
  .toString()
  .trim()
  .split('\n')
  .map((e) => e.split(' ').map((v) => +v));

let S = 0;
let E = 1;

const solution = (rawInputs) => {
  const [[n], ...arr] = rawInputs;
  let answer = 0;
  // a: 시작 달, b: 시작 날짜, c: 끝 달, d: 끝 날짜
  let dates = arr
    .map(([a, b, c, d]) => [a * 100 + b, c * 100 + d])
    .sort((a, b) => (a[0] === b[0] ? a[1] - b[1] : a[0] - b[0]));

  let last = 301;

  while (dates.length > 0) {
    // last가 범위 넘으면 종룍 ㅏ능
    if (last >= 1201) break;

    let temp = 0;
    let idx = 0;
    for (let i = 0; i < dates.length; i++) {
      // 꽃ㅇ ㅣ피는 날짜가 last보다 빨라야함
      if (dates[i][S] <= last) {
        // 같아도 되나,,?
        // if (dates[i][S] < last) {
        // 가장 느린 날 확인
        if (temp <= dates[i][E]) {
          temp = dates[i][E];
          idx = i;
        }

        continue;
      }
      break;
    }

    last = temp;
    dates = dates.slice(idx + 1);
    answer++;
  }

  if (last < 1201) return 0;

  return answer;
};

console.log(solution(rawInputs));

module.exports = { solution };
