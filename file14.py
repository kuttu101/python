# Palindrome
# x=input("enter the number")
# if x==x[::-1]:
#  print("True")
# else:
#  print("False")


#  Merge two sorted lists
# list1=[1,2,4]
# list2=[1,3,4]
# list3=list1+list2
# list3.sort()
# print (list3)


# Remove duplicate elements from a sorted array
# num=[0,0,1,1,1,2,2,3,3,3,4]
# a=set(num)
# b=list(a)
# print(len(b),"num=",b)


# Remove element
# num=[1,2,3,4,5,3,6,7,3]
# value=3

# for i in num:
#     if i==value:
#         num.remove(i)
    
# print("number of elements=",len(num))
# print(num)


# Reverse linked list
# a=[1,2,3,4,5]
# print(a)
# b=a[::-1]
# print(b)


# Contains duplicate
# a=[1,2,3,4,3,2,5]
# b=set(a)
# if a==b:
#     print("False")
# else:
#     print("True")


# Length of the last word
# a="python programs are interesting"
# b=a.strip()
# c=b.split()
# d=c[-1]
# print("the last word is ",d,"and the length of that word is",len(d))


#Number of segments in a string
# a="hello world"
# b=a.split()
# print(len(b))


#Is subsequence
# a="ever"
# b="for"
# if a in b:
#         print('true')
# else:
#         print('false')


#Search insert position
# a=input("enter the numbers in order")
# b=list(a)
# n=(input("enter the number"))
# if n in b:
#     print(b.index(n))


# Third maximum number
# a=[10,12,14,16,18,20]
# b=len(a)

# c=int(0)
# for i in range(1,b):
#         if(a[i]>c):
#             c=a[i]
 
# d=int(0)
# for i in range(0,b):
#         if(a[i]>d and
#             a[i]<c):
#             d=a[i]

# e=int(0)
# for i in range(0,b):
#         if(a[i]>e and
#             a[i]<d):
#             e=a[i]         
 
# print("The first maximum number is",c)
# print("The second maximum number is",d)
# print("The third maximum number is",e)



