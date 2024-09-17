def merge_sort(a):
    if len(a) <= 1:
        return a

    mid = len(a) // 2
    leftList = merge_sort(a[:mid])
    rightList = merge_sort(a[mid:])

    return merge(leftList, rightList)

def merge(leftList, rightList):
    sorted_list = []
    i = j = 0

    while i < len(leftList) and j < len(rightList):
        if leftList[i] < rightList[j]:
            sorted_list.append(leftList[i])
            i += 1
        else:
            sorted_list.append(rightList[j])
            j += 1

    while i < len(leftList):
        sorted_list.append(leftList[i])
        i += 1

    while j < len(rightList):
        sorted_list.append(rightList[j])
        j += 1

    return sorted_list

a = [6, 8, 3, 9, 1, 2, 0, 7, 4]
print(merge_sort(a))
