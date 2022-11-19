# function defination
def mergeSortedArrays(arr1, arr2, n1, n2, final):
    i = 0
    j = 0
    k = 0

    # traversing arr1 and inserting in final array
    while (i < n1):
        final[k] = arr1[i]
        k = k + 1
        i = i + 1

   # traversing arr2 and inserting in final array
    while (j < n2):
        final[k] = arr2[j]
        k = k + 1
        j = j + 1
    final.sort()  # sorting the final array


arr1 = [10, 30, 50, 70, 90]
n1 = len(arr1)

arr2 = [20, 40, 60, 80]
n2 = len(arr2)

final = [0] * (n1+n2)

mergeSortedArrays(arr1, arr2, n1, n2, final)

print("After merging: ")

for i in range(n1 + n2):
    print(final[i], end=" ")
