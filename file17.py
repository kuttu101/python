student={}
prn=2000210
stdlist=[]
teacher={}
trslist=[]
while True:
    print('1.student name','2.view student details','3.teacher name','4.view teachers details','5.exit')
    choice=int(input('enter your choice'))
    if choice==1:
        stdname=input('enter your name')
        student['stdname']=stdname
        stdage=int(input('enter the age'))
        student['stdage']=stdage
        dept=input('enter the department')
        student['dept']=dept
        student['prn']=prn
        stdlist.append(student.copy())
    if choice==2:
        for i in stdlist:
            print('-'*20)
            for j,k in i.items():
                print(j,':',k)
            for i in stdlist:
                print('-'*20)
    if choice==3:
        trsname=input('enter the teachers name')
        teacher['trsname']=trsname
        trsdept=input('enter the teacher department')
        teacher['trsdept']:trsdept
        trslist.append(teacher.copy())
    if choice==4:
         for i in stdlist:
            print('-'*20)
            for j,k in i.items():
                print(j,':',k)
            for i in trslist:
                print('-'*20)
    if choice==5:
        exit()