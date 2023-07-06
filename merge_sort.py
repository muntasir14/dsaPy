def merge(l1, l2):
    count1 = len(l1)
    count2 = len(l2)
    result = []
    i = 0
    j = 0

    while i < count1 or j < count2:
        if l1[i] < l2[j]:
            result.append(l1[i])
            i += 1
        elif l1[i] >= l2[j]:
            result.append(l2[j])
            j += 1

        if i == count1:
            while j < count2:
                result.append(l2[j])
                j += 1
            break
        elif j == count2:
            while i < count1:
                result.append(l1[i])
                i += 1
            break

    print("merged", result)
    return result


def merge_sort(l):
    print(l)
    count = len(l)
    if count == 1:
        return l
    elif count == 2:
        if l[0] > l[1]:
            l[0], l[1] = l[1], l[0]
        print("2 len suffled", l)
        return l
    mid = int(count / 2)
    print("divide mid", mid)
    print("1st half", l[0:mid])
    print("2nd half", l[mid:count])
    return merge(merge_sort(l[0:mid]), merge_sort(l[mid:count]))


# print(merge_sort([21, 4, 1, 3, 9, 20, 25]))
print(merge_sort([2, 3, 1, 6, 9, 4]))
