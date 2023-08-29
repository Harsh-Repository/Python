#check if an array is sorted or not using recursion
# def isSorted(a):
#     l = len(a)
#     if l == 0 or l == 1:
#         return True
#     if a[0] > a[1]:
#         return False
#     smallerList=a[1:]
#     isSmallerListSorted=isSorted(smallerList)
#     if isSmallerListSorted:
#         print (True)
#     else:
#         print (False)

# a=[1,2,3,4,9,5,6]
# isSorted(a)

def isSortedBetter(a, si):
    l = len(a)
    if si == l-1 or si == l:
        print (True)
    if a[si] > a[si+1]:
        print (False)
    isSmallerPartSorted = isSortedBetter(a, si+1)
    return isSmallerPartSorted
a= [1,2,3,5,7,9,8] 
isSortedBetter(a,5)