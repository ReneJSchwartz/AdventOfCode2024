import re
import random

file = open("real_rules")  # open("example_rules")
rules = file.readlines()
#print(rules)
for i in range(len(rules)):
    rules[i] = re.findall(r'\d+', rules[i])
#print(rules)

file = open("real_updates")  # open("example_updates")
updates = file.readlines()
for i in range(len(updates)):
    updates[i] = re.findall(r'\d+', updates[i])
#print(updates)

sum = 0
sum_reshuffled = 0
invalid_updates = []
for update in updates:
    # nums = re.findall(r'\d+', update)
    #print(update)
    # go through all rules and see if apply
    valid = False
    double_break = False
    for rule in rules:
        if set(rule).issubset(update):
            # print(rule, "is in", update)
            # first number in rule must be before second
            for num in update:
                #print(str(num))
                if num == rule[0]:
                   valid = True
                   break
                elif num == rule[1]:
                    #print("second number came before first")
                    valid = False
                    double_break = True
                    #invalid_updates.append(update)
                    break
            if double_break:
                #print("double breaking")
                break
    if valid:
        # look for the middle one
        #print("Was valid. Middle element: " + update[int(len(update) / 2)])
        #sum += int(update[int(len(update) / 2)])
        pass
    else:
        #part 2
        #reorder and get middle element of invalid ones
        #reorder some sort of sort
        for i in range(len(update)):
            #random sort and see if pass
            random.shuffle(update)
            double_break = False
            valid = False
            for rule in rules:
                if set(rule).issubset(update):
                    for num in update:
                        if num == rule[0]:
                           valid = True
                           break
                        elif num == rule[1]:
                            # first number in rule must be before second
                            for i in range(len(update) - 1, 0, -1):
                                if update[i] == rule[1]:
                                # todo add p2 sort logic here (switch to left side)    
                                pass
                                
                            valid = False
                            double_break = True
                            break
                    if double_break:
                        break
            
        sum_reshuffled += int(update[int(len(update) / 2)])
    
# print("sum of valid update middle elements is: " + str(sum))
print("sum of reshuffled update middle elements is: " + str(sum_reshuffled))
        
    
