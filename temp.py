
import libs.common.accuracy as ac
import libs.common.algebra as a
import libs.common.sorting as s

print( ac.sensitivity(5,3))


print(a.norm([6,7],[1,3],1))
print(a.norm([6,7],[3,3],2))
print(a.norm([6,7],[1,3],3))


x= [3, 9,11, 15, 4 ,6, 3,2,6,7,8,23, 1 ]

print(a.median(x))

arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
s.quickSort(arr, 0, n - 1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i]),

    # This code is contributed by Mohit Kumra
