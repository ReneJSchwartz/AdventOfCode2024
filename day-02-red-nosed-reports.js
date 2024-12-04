const example = `7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9`;

const realData = `1 2 3`;

const data = realData;
//const data = example;

const numRows = data.split('\n');

let safeAmt = 0;

for (let i = 0; i < numRows.length; i++) {
  const nums = numRows[i].split(' ').map(Number);
  let isSafe = true;

  const increasing = nums[0] < nums[1];
  const decreasing = nums[0] > nums[1];
  if (!increasing && !decreasing) {
    continue;
  }

  for (let j = 0; j < nums.length - 1; j++) {
    const delta = nums[j] - nums[j + 1];
    if (increasing && delta > -1) {
      isSafe = false;
      break;
    }
    if (increasing && delta < -3) {
      isSafe = false;
      break;
    }
    if (decreasing && delta < 1) {
      isSafe = false;
      break;
    }
    if (decreasing && delta > 3) {
      isSafe = false;
      break;
    }
  }
  if (isSafe) {
    safeAmt++;
  }
}

console.log('Safe rows: ' + safeAmt);

// Part 2: apply problem dampener which can remove a single bad number from a row

safeAmt = 0;

for (let i = 0; i < numRows.length; i++) {
  const nums = numRows[i].split(' ').map(Number);
  let isSafe = false;

  // process row
  for (let j = 0; j < nums.length; j++) {
    let array = nums.map(x => x);
    array.splice(j, 1);

    const increasing = array[0] < array[1];
    const decreasing = array[0] > array[1];

    if (!increasing && !decreasing) {
      continue;
    }

    let safe = true;

    for (let i = 0; i < array.length - 1; i++) {
      const delta = array[i] - array[i + 1]; 
      // delta must be between 1-3 in either 
      // plus or minus direction
      if (increasing && delta > -1) {
        safe = false;
        break;
      }
      if (increasing && delta < -3) {
        safe = false;
        break;
      }
      if (decreasing && delta < 1) {
        safe = false;
        break;
      }
      if (decreasing && delta > 3) {
        safe = false;
        break;
      }
    }


    if (safe)
    {
      isSafe = true;
      break;
    }
  }

  if (isSafe === true) {
    safeAmt++;
  }
}

console.log('Part 2 dampened safe rows: ' + safeAmt);
