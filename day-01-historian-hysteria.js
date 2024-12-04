const str = `3   4
4   3
2   5
1   3
3   9
3   3`;

// Put numbers to an array.
let nums = str.split("\n");
nums = nums.join().split(/\D/).filter((word) => word.length > 0);

// separate by left and right column
let left = [];
let right = [];

for (let i = 0; i < nums.length; i++) {
  if (i % 2 === 0)
  {
    left.push(nums[i]);
  }
  else
  {
    right.push(nums[i]); 
  }
}

// change to numbers from string and sort non-alphabetically
left = left.map(Number);
left.sort((a, b) => (a - b));

right = right.map(Number);
right.sort((a, b) => (a - b));

// start counting answer by calculating the difference 
// between smallest numbers
let ans = 0;

for (let i = 0; i < left.length; i++) {
  ans += Math.abs(left[i]-right[i]);
}

console.log("p1: " + ans);

// Part 2 count how many times each thing in left appears in right and multiply ans by it
ans = 0;

for (let i = 0; i < left.length; i++) {
  const num = left[i];
  let appearsTimes = 0;

  right.forEach((element) => { 
    if (element === num)
    {
      appearsTimes++;
    }
    });
  
  ans += appearsTimes * num;    
}

console.log("p2: " + ans);
