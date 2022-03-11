
def erfen(list1, num):
    low = 0
    high = len(list1) - 1
    while low <= high:
        mid = (low + high ) // 2
        if(list1[mid] == num):
            return mid
        elif(list1[mid] < num):
            low = mid + 1
        else:
            high = mid - 1
    return None

if __name__ == '__main__':
    my_list = [1,3,5,7,9]
    print(erfen(my_list,3))
    print(erfen(my_list, -1))

    #O(logn)