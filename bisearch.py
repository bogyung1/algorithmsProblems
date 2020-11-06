# divide&Conquer
# Binary Search
# Recursive Algorithm, 재귀적 알고리즘

def binary_search(array, target, low, high):
    mid= (low+high)//2
    middle=array[mid]
    if target==middle:
        print('target position %d' %mid)
    elif middle>target:
        binary_search(array, target, low, mid-1)
    elif middle<target:
        binary_search(array, target, mid+1, high)
    else:
        return False


target= 30
list=[20, 26, 47, 35, 85, 33, 30, 72, 74]
length=len(list)

list.sort()
left=0
right=length-1

binary_search(list, target, left, right)
