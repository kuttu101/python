# missing numbers
# list=[1,3,5,7,9,11]
# for i in range(12):
#     if i not in list:
#         print (i)

# add digits
# a=135
# sum=0
# for i in str(a):
#     sum+=int(i)
# print (sum)

# letter combination of a phone number

list={1:"&",2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz",0:"_"}
a=int(input('enter the numbers'))

if a<=9:
    b=list[a]
    for i in b:
        print(i)

if a>9 and a<100:
    c=a//10
    d=a%10
    e=list[c]
    f=list[d]
    for i in e:
        for j in f:
            print(i+j)
        print("")





    

   



