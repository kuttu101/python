student={}
prn=2000210
studentlist=[]
teachlist=[]
studentstore=[]
teachstore=[]
while True:
    print('1.student name','2.teacher details','3.view student','4.view teacher','5.view assigned','6.','7.fees','8.exit()')
    choice=int(input('enter your choice'))
    if choice==1:
        name=input("enter your name:")
        student["name"]=name
        age=int(input("enter the age:"))
        student["age"]=age
        studentdepartment=input('enter the department')
        student["prn"]=prn
        prn+=1
        studentlist.append(student.copy())
    if choice==2:
        name=input("enter the name:")
        teachlist.append(name)
    if choice==3:
        print(studentlist)
    if choice==4:
        print(teachlist)
    if choice==5:
        student=input('enter student name')
        for i in studentlist:
            studentstore.append(i['name'])
        b=len(teachlist)
        for j in range(b):
            if student in studentstore:
                for i in studentlist:
                    if i['name']==student:
                        i['teachstore']=teachlist[j]
        for i in studentlist:
            print('-'*20)
            for j,k in i.items():
                print(j,':',k)
                print('-'*20)
    if choice==6:
        student=input('enter the department')
        for i in studentlist:
            studentstore.append(i['studentdepartment'])
        if student in studentstore:
             for i in studentlist:
                    if i['studentdepartment']==student:
                        for n in teachlist:
                            i['teachstore']=teachlist[0]
                    else:
                            i['teachstore']=teachlist[1]
        for i in studentlist:
            print('-'*20)
            for j,k in i.items():
                print(j,':',k)
            print('-'*20)
    if choice==7:

    if choice==8:
        exit()