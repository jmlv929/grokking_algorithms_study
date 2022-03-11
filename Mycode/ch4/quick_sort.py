
def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        less = [i for i in arr[1:] if i < arr[0]]
        big = [i for i in arr[1:] if i >= arr[0]]
        return quick_sort(less) + [arr[0]] + quick_sort(big)

if __name__ == "__main__":
    list1 = [1,4,2,5,9,0]
    print(quick_sort(list1))

    #平均时间 以及 最佳时间O(nlogn)  最坏 O(n^2)