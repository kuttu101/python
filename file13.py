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


a=[2,6,5,4]
sum=10
b=[]
for i in range(0,len(a)):
    for j in range(i+1,len(a)):
     if a[i]+a[j]==sum:
        b.append(i)
        b.append(j)
        print(b)
