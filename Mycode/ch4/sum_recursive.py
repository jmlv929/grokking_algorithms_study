def sum(list1):
    if(list1 == []):
        return 0
    else:
        return list1[0] + sum(list1[1:])

if __name__ == "__main__":
    my_list = [1,24,4,7,9,10]
    print(sum(my_list))