bank={}
account_num=1234
balance=0
details=[]
while True:
    print("1.create account","2.view account","3.exit")
    choice=int(input('enter your choice'))
    if choice==1:
        name=input('enter your name')
        bank["name:"]=name
        age=int(input('enter your age'))
        bank["age:"]=age
        contact=int(input('enter your number'))
        bank["contact:"]=contact
        bank["account number:"]=account_num
        account_num=account_num+1
        bank["balance:"]=balance
    elif choice==2:
        details.append(bank.copy())
        print(details)
        
    elif choice==3:
        exit()
