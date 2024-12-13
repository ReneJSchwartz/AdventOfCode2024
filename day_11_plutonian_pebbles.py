import re

#example = "0 1 10 99 999"
example = "125 17"
stones = re.findall(r"\d+", example)
stones = [int(stone) for stone in stones]
#print(stones)
newArr = []

blinks = 25
for blink in range(blinks):
    for i in range(len(stones)):
        stone = stones[i]
        if stone == 0:
            newArr.append(1)
        elif len(str(stone)) % 2 == 0:
            w = str(stone)
            newArr.append(int(w[:len(w)//2]))
            newArr.append(int(w[len(w)//2:]))
        else:
            newArr.append(stone * 2024)
        
    stones = newArr
    newArr = []

#print(stones)
print(len(stones))
