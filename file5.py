# a= int(input("enter any number"))
# for i in range(1,a+1):
#         for j in range(1,i+1):
#             print(j,end='')
#         print('')        
# n= int(input("enter row"))
# num=1
# for i in range(1,n):
#     for j in range (1,i+1):
#      print(j,end=" ")
#     num=num+1
#     print('')        
# n=1
# a=int(input("enter the row"))
# for i in range(0,a):
#     for j in range(i):
#         print(n,end=" ")
#         n=n+1
#     print('')
a=int(input('enter any number'))
print('*')
for i in range (1,a+1):
    for j in range (1,i):
        print (j,end='')
    for k in range (i,0,-1):
        print (k,end='')
        print('*')