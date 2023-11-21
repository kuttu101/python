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
    n=list[a]
    for i in n:
        print(i)

if a>9 and a<100:
    n1=a//10
    n2=a%10
    n3=list[n1]
    n4=list[n2]
    for i in n3:
        for j in n4:
            print(i+j)
        print("")

if a>99 and a<1000:
    n5=a//10
    n6=a%10
    n7=a//10
    n8=list[n5]
    n9=list[n6]
    n10=list[n7]
    for i in n8:
        for j in n9:
            for k in n10:
                print(i+j+k)
            print("")
            





    

   



