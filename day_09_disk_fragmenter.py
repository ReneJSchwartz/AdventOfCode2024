# day_09_disk_fragmenter.py

disk_map_dense = "2333133121414131402"
x = open("input")
# x = open("example")
disk_map_dense = x.read()

disk_map = ""

even_odd_counter = 0
file_counter = 0
for x in disk_map_dense:
    if even_odd_counter % 2 == 0:
        disk_map += str(file_counter % 10) * int(x)
        file_counter += 1
    else:
        disk_map += "." * int(x)
        pass

    even_odd_counter += 1

disk_map = list(disk_map)

#replace all dots with last number (until dot index has passed last num index)
last_num_index = 0
last_num = '7'

# i/index was not working with list element assignment, the weirdest bug I've seen to date so this is just a duplication of i
counter = 0
for index in range(len(disk_map)):
    if disk_map[index] == '.' and index < len(disk_map) - last_num_index:  #and i < len(disk_map) - last_num_index_negative:  # possible off by one error
        # print(index)
        # get last num
    
        # calculate inline due to skill issues, cough I mean performance reasons
        for i in range(last_num_index, len(disk_map)):
            if disk_map[-(i + 1)] != '.':
                last_num_index = i + 1
                last_num = disk_map[-last_num_index]
                break
            
        # print("putting " + str(last_num) + " to index " + str(index))
        # print(''.join(disk_map))
        # index 2 puts element to zeroeth element so we're using this counter???
        disk_map[counter] = last_num
        disk_map[-last_num_index] = '.'
        # print(''.join(disk_map))
        
    counter += 1
    
print(''.join(disk_map))

# calculate checksums
sum = 0
for i in range(len(disk_map)):
    if disk_map[i] != '.':
        sum += i * int(disk_map[i])
        
# p1, correct on example but not correct on input. final sequence lgtm.
print(sum)
