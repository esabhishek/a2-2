file_handle = open( "clustering2.txt", "r" )
str = file_handle.readline()
num_nodes = int(str.split()[0])
num_bits = int(str.split()[1])

print num_nodes
print num_bits

cluster_array = []

setbit_list = []

for ctr in range(0, num_bits + 1):
    temp = []
    setbit_list.append(temp)

str = file_handle.readlines()
i = 0
merge_count = 0
for line in str:
    line = line.replace(' ', "")
    line = line.replace('\n', "")
    temp = []

    temp.append(line)

    index = line.count("1")
    merge = []
    head = []

    for ctr in range(index -  2, index + 3):
        for loop in setbit_list[ctr]:

            if bin(int(loop[0], 2) ^ int(line, 2)).count("1") <= 2:
               if not (cluster_array[loop[1]][1] in head):
                    for ctr1 in cluster_array[loop[1]][1]:
                        merge.append(ctr1)
                    head.append(cluster_array[loop[1]][1])
                    merge_count += 1

    merge.append(i)
    temp.append(merge)
    cluster_array.append(temp)
    for loop in merge:
        cluster_array[loop][1] = merge
    temp1 = []
    temp1.append(line)
    temp1.append(i)
    setbit_list[index].append(temp1)
    i += 1

print num_nodes - merge_count