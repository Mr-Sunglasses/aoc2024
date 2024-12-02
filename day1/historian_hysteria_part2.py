from pathlib import Path

def format_file_and_return_array(filename: Path):

    with open(filename) as f:
        list1 = []
        list2 = []
        buffer = f.readlines()
        for i in buffer:
            temp = i.replace("\n", "").split()
        
            list1.append(int(temp[0]))
            list2.append(int(temp[1]))
        
        list1.sort()
        list2.sort()
        return list1, list2

def sum_similar_distances(arr1, arr2):
    dis = []
    # for i, j in zip(arr1, arr2):
    #     dis.append(abs(j-i))
    for i in range(len(arr1)):
        dis.append(arr1[i] * abs(arr2.count(arr1[i])))
    return sum(dis)

# print(format_file_and_return_array(filename="input.txt"))
arr1, arr2 = format_file_and_return_array(filename="input2.txt")
print(sum_similar_distances(arr1, arr2))