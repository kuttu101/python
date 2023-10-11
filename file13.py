# Two sum
# a=[4,2,3]
# sum=6
# b=[]
# if a[0]+a[1]==sum:
#     b.append(0)
#     b.append(1)
#     print(b)

# elif a[1]+a[2]==sum:
#      b.append(1)
#      b.append(2)
#      print(b)

# elif a[2]+a[0]==sum:
#      b.append(2)
#      b.append(0)
#      print(b)

# else:
#     print("the entered data is invalid")

# a=[2,6,5,4]
# sum=10
# b=[]
# for i in range(0,len(a)):
#     for j in range(i+1,len(a)):
#      if a[i]+a[j]==sum:
#         b.append(i)
#         b.append(j)
#         print(b)


# Add binary
# a='111'
# b='101'
# sum=bin(int(a,2)+int(b,2))
# print(sum[2:])


# add two integers
# a=int(input("enter the number"))
# b=int(input("enter the number"))
# sum=a+b
# print("sum of",a,"and",b,"is",sum)


# Majority element
# a=[1,2,3,3,3,3,4,5,6,3,3,3]
# b=len(a)
# for i in range(b):
#         if a.count(i)>b/2:
#                print("The majority element is",i,"with",a.count(i),"occurences")
    

# Reverse string
# list=['a','p','p','l','e']
# print(list[::-1])


# Climbing stairs
# n=int(input("enter the number of stairs to be climbed"))
# b=1
# c=1


# Plus one
a=[1,3,9]
b=len(a)
index=b-1
while(index>=0 and a[index]==9):
    a[index]=0
    index-=1

    if(index<0):
        a.insert(0,1)
    else:
        a[index]+=1
print(a)
    


