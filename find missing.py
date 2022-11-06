def find_missing(lst, n):
    left = 0
    right = len(lst)-1
    while left<=right:
        midle = (left+right)//2
        if lst[midle] == midle:
            left = midle+1
        else:
            right = midle-1
    return left


def find(lst, s):
    n = len(lst)
    low = 0
    high = n-1
    while low<=high:
        midle = (low+high)//2
        if lst[midle] == s:
            return midle
        if lst[low]<lst[midle]:
            if lst[low]<=s<lst[midle]:
                high = midle-1
            else:
                low = midle+1
        else:
            if lst[midle]<s<=lst[high]:
                low = midle+1
            else:
                high = midle -1
    return None


def find2(lst, s):
    for i in range(len(lst)):
        if lst[i] == s:
            return i
    return None

