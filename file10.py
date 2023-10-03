# To display the sum of the inputted elements by the user

# a=int(input("enter the limit"))
# sum=0
# for i in range(a):
#     b=int(input("enter the number"))
#     print(b)
#     sum+=b
# print("the total sum",sum)
    

# To count the number of duplicate elements in a given list
    
a=[1,2,5,7,3,1,3,2,4,8]
# real=set(a)
# len(real)
# dupli=len(a)-len(real)
b=[]
for i in a:
    if a.count(i)>1:
        b.append(i)
print("the duplicate elements are",b)

    

