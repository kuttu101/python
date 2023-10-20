bank={}
account_no=1234
balance=0
details=[]
acc=[]
while True:
    print("1.create account","2.view account","3.add balance","4.withdraw balance","5.exit")
    choice=int(input('enter your choice'))
    if choice==1:
        name=input('enter your name')
        bank["name:"]=name
        age=int(input('enter your age'))
        bank["age:"]=age
        contact=int(input('enter your number'))
        bank["contact:"]=contact
        bank["account number:"]=account_no
        account_no=account_no+1
        bank["balance:"]=balance
        details.append(bank.copy())
    elif choice==2:
         for i in details:
              print('_'*10)
              for key,value in i.items():
                   print(key,':',value)
                   print('_'*10)
             
    elif choice==3:
        account_no=int(input("enter your account number"))
        amount=int(input("enter the amount"))
        for i in details:
            acc.append(i['account number:'])
        if account_no in acc:
               for i in details:
                   if i['account number:']==account_no:
                      i['balance:']+=amount
        else:
                       print('account not accessible')
    elif choice==4:
         account_no=int(input("enter your account number"))
         amount=int(input("enter the amount"))
         for i in details:
          acc.append(i["account number:"])
         if account_no in acc:
             for i in details:
                 if i['account number:']==account_no:
                     if i['balance:']<balance:
                      i['balance:']-=amount
                     else:
                           print("not possible")
    elif choice==5:
        exit() 