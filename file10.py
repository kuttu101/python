# PART TWO

# 1.Grade calculator
# a=int(input("enter any number"))
# if a>=90:
#          print("Grade is A") 
# elif a>=80:
#        print("Grade is B")
# elif a>=70:
#         print("Grade is C")
# elif a>=60:
#         print("Grade is D")
# else:
#        print("Grade is F")

#2.Calculator
# a=int(input("enter a digit")) 
# b=int(input("enter a digit")) 
# operator=input("enter your operation")
# if operator == "+":
#     sum=a+b
#     print("the sum of",a,"and",b,"is",sum) 
# elif operator=="-":
#     subtract=a-b
#     print("the difference of",a,"and",b,"is",subtract)
# elif operator == "*":
#     product=a*b
#     print ("the  product of",a,"and",b,"is",product)
# elif operator=="/":
#     quotient = a/b
#     print ("the quotient of",a,"and",b,"is",quotient)
# else:
#     print("operator not assigned")

# 3.Age identifier
# a=int(input("type the age"))
# if a<=2:
#   print("infant")
# elif a<=12:
#   print("child")
# elif a<=19:
#   print("teenager")
# elif a<=64:
#   print("adult")
# elif a>65:
#   print("senior")
# else:
#   print("input not valid")

# 4.BMI Calculator
# weight=float(input("enter your weight"))
# height=float(input("enter your height"))
# bmi=weight/height
# if bmi<18.5:
#     print("underweight")
# elif bmi<=24.9:
#     print("normal weight")
# elif bmi<=29.9:
#     print("overweight")
# else:
#     print("overweight")
    
# 6.Largest
# a=int(input("enter a digit"))
# b=int(input("enter a digit"))
# c=int(input("enter a digit"))
# if a>b and a>c:
#  print(a,"is the largest number")
# elif b>a and b>c:
#  print(b,"is the largest number")
# else:
#  print(c,"is the largest number")

#7.Weekdays
# a=int(input("enter the number"))
# if a==1:
#     print("Monday")
# elif a==2:
#     print("Tuesday")
# elif a==3:
#     print("Wednesday")
# elif a==4:
#     print("Thursday")
# elif a==5:
#     print("Friday") 
# elif a==6:
#     print("Saturday")
# elif a==7:
#     print("Sunday")
# else:
#     print("Invalid input")

#8.Identify
a=input("enter any key")
if a is a.upper:
    print(a,"is an alphabet and is in uppercase")
elif a is a.lower:
    print(a,"is an alphabet and is in lowercase")
elif a is a.isdigit:
    print(a,"is a digit")
elif a is a.isalnum:
    print(a,"is a special character")
else:
    print("Invalid input, kindly input just one key")