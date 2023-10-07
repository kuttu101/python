# To display the sum of the inputted elements by the user

# a=int(input("enter the limit"))
# sum=0
# for i in range(a):
#     b=int(input("enter the number"))
#     print(b)
#     sum+=b
# print("the total sum",sum)
    

# To count the number of duplicate elements in a given list
    
# a=[1,1,2,3,4,5,6,1,3,7]
# # real=set(a)
# # len(real)
# # dupli=len(a)-len(real)
# b=[]
# for i in a:
#     if a.count(i)>1:
#         b.append(i)
# print("the duplicate elements are",b)
# b.sort()
# print(b)
# c=b.count(1)
# d=b.count(3)
# print("1 appears",c,"times")
# print("3 appears",d,"times")

a=[1,1,2,3,4,5,6,1,3,7,4,4]
b=[]
for i in a:
     if a.count(i)>1:
         b.append(i)
print("the duplicate elements are",b)
b.sort()
print(b)

          


