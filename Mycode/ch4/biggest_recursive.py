def biggest_recursive(list_1):
    if list_1 == []:
        return None
    elif len(list_1) == 1:
        return list_1[0]
    elif len(list_1) == 2:
        return  list_1[0] if list_1[0] > list_1[1] else list_1[1]
    else:
        return list_1[0] if list_1[0] > biggest_recursive(list_1[1:]) else biggest_recursive(list_1[1:])

if __name__ == "__main__":
    my_list1 = [2,4,6,3,8,3,9,45,98,36]
    my_list2 = [2, 4]
    my_list3 = []
    print(biggest_recursive(my_list1))
    print(biggest_recursive(my_list2))
    print(biggest_recursive(my_list3))