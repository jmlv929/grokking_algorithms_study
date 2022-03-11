
def cal(list_1):
    if(list_1 == []):
        return 0
    else:
        return 1 + cal(list_1[1:])


if __name__ == "__main__":
    my_list = [1,2,3,4,5,6]
    print(cal(my_list))