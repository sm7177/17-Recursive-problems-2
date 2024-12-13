# def ways(stairs):
#     if stairs<0:
#         return 0
#     if stairs==0:
#         return 1
#     twosteps=0
#     onestep=0

#     if (stairs>=2):
#         twosteps=ways(stairs-2)
#     onestep=ways(stairs-1)
#     return twosteps +onestep

# stairs=int(input("Enter stairs:"))

# print(ways(stairs))










# def paren(s,l,r,p,n):
#     if (p==2*n):
#         for ss in s:
#             print(ss,end="")
#         print("\n")
#         return
#     if (l>r):
#         s[p]="}"
#         paren(s,l,r+1,p+1,n)
#     if (l<n):
#         s[p]="{"
#         paren(s,l+1,r,p+1,n)

# n=int(input("Enter the number for brackets: "))

# s=[""]*2*n
# print("\n")
# paren(s,0,0,0,n)






def count_occurrences(arr,target,index=0):
    if index==len(arr): 
        return 0
    count=1 if arr[index]==target else 0
    return count + count_occurrences(arr,target,index+1)

print(count_occurrences([1,2,3,2,2,4],2))
# print(count_occurrences([1,3,5,7,9]))