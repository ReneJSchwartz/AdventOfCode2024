# day_13_claw_contraption.py
"""Calculates how many tickets you need to use to get jackpots from claw machines.

Uses DFS to find combinations of button presses that result in a jackpot.
"""

from typing import List
import math

x = open("input").read()
machines = x.split("\n\n")

for machine in machines:
    pass
    
# following code is taken from neetcode combination sum
def combinationSum(nums: List[int], target: int) -> List[List[int]]:
    res = []

    def dfs(i, cur, total):
        if total == target:
            res.append(cur.copy())
            return
        if i >= len(nums) or total > target:
            return

        cur.append(nums[i])
        dfs(i, cur, total + nums[i])
        cur.pop()
        dfs(i + 1, cur, total)

    dfs(0, [], 0)
    return res

# example values, need to be looped
nums = [94,22] 
target = 8400
combinations = combinationSum(nums, target)
lowest = math.inf
for comb in combinations:
    token_cost = comb.count(nums[0]) * 3 + comb.count(nums[1])
    if token_cost < lowest:
        lowest = token_cost

# prints 280 tokens
print(lowest)

# todo: see if y calcs have a matching combination with intersection()
# and only use those. sum or sort if needed. 
