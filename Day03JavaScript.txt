const example = 'xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))';
const realData = String.raw`123`;

let dataSource = example;

let occurrences = [];

const mulRe = /mul\(\d{1,9999},\d{1,9999}\)/gm;

occurrences = dataSource.match(mulRe);

console.log(occurrences);

let multiplicationSum = 0;

for (let i = 0; i < occurrences.length; i++)
{
	  const numsRe = /\d{1,9999}/g;
  	let nums = occurrences[i].match(numsRe);
  	nums = nums.map(Number);

  	multiplicationSum += nums[0] * nums[1];
}

console.log(multiplicationSum);

// Day 3 Part 2
console.log("Part 2");
multiplicationSum = 0;
const example2 = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"; 

dataSource = realData;

const mulDoDontRe = /mul\(\d{1,9999},\d{1,9999}\)|do\(\)|do\(\)|don\'t\(\)/gm;

occurrences = dataSource.match(mulDoDontRe);

console.log(occurrences);

let multiply = true;
for (let i = 0; i < occurrences.length; i++)
{
  	if (occurrences[i].substring(0, 3) === "mul" && multiply)
    {
  		const numsRe = /\d{1,9999}/g;
    	let nums = occurrences[i].match(numsRe);
    	nums = nums.map(Number);
    	multiplicationSum += nums[0] * nums[1];
    }
  	if (occurrences[i].substring(0, 3) === "do(")
    {
      multiply = true;
    }
  	if (occurrences[i].substring(0, 3) === "don")
    {
      multiply = false;
    }
}

console.log("p2: " + multiplicationSum);
