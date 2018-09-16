
import libs.Math.Accuracy as ac
import libs.Math.Algebra as a

print( ac.Sensitivity(5,3))


print(a.norm([6,7],[1,3],1))
print(a.norm([6,7],[3,3],2))
print(a.norm([6,7],[1,3],3))


x= [3, 9,11, 15, 4 ,6, 3,2,6,7,8,23, 1 ]

print(a.median(x))