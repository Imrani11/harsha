'''
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The relative order of the elements may be changed.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.
'''


def deleteElement(arr, n, x):
    for i in range(n):
        if (arr[i] == x):
            break
    if (i < n):
        n = n - 1
        for j in range(i, n, 1):
            arr[j] = arr[j + 1]
    return n
if __name__ == '__main__':
    arr = [11, 15, 6, 8, 10]
    n = len(arr)
    x = 6
    n = deleteElement(arr, n, x)

    print("Modified array is")
    for i in range(n):
        # if arr[i] == x:
        #     del arr[i]
        print(arr[i], end=" ")


