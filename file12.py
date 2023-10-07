# string="ABABABAABBAABBB"
# c=0
# for i in string:
#     if i=='A':
#         c+=1
#     elif i=='B':
#         c-=1

# if c==0:
#       print("balanced")
# else:
#       print("unbalanced")
    
# #  if i=='A':
# #      c+=1
# # if i=='B':
# #      c-=1
# # if c==0:
# #      print("balanced")
# # else:
# #       print("unbalanced")   


# a=[2,4,3,1]
# a.reverse()
# print(a)
# a.insert(1,2)
# print(a)
# a.pop(4)
# print(a)



listnum= int(input("enter the number of elements"))
num=[]

for i in range (listnum):
    for j in range(i + 1, listnum):
        if(num[i]>num[j]):
            temp = num[i]
            num[i] =num[j]
            num[j] = temp

print(num)


