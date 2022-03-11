

def find_biggest(arr):
    biggest = arr[0]
    big_index = 0
    for i in range(1, len(arr)):
        if(arr[i] > biggest):
            biggest = arr[i]
            big_index = i
    return big_index

def zuhe(arr):
    my_arr = []
    for i in range(len(arr)):
        my_arr.append(arr.pop(find_biggest(arr)))
    return my_arr



if __name__ == "__main__":
    my_list = [2,4,6,9,4,5,8]
    print(zuhe(my_list))
# O(n^2)