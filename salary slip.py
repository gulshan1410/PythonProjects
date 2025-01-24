name=input("Enter emp name :")
eid=input("Enter id :")
bs=int(input("Enter basic salary :"))
if bs>=20000:
    ta=bs*70//100
    da=bs*50//100
    hra=bs*30//100
elif bs>=15000:
    ta=bs*50//100
    da=bs*30//100
    hra=bs*20//100
elif bs>=10000 :
    ta=bs*40//100
    da=bs*20//100
    hra=bs*15//100

else:
    ta=bs*30//100
    da=bs*10//100
    hra=bs*12//100
gs=bs+ta+da+hra
tds=gs*10/100
ns=gs-tds
print("-----------------------------------------------------------------------------------------------------------------")
print("\t\t\tSalary slip of ",name)
print("-----------------------------------------------------------------------------------------------------------------")
print(" Emp id is",eid)
print("basic salary is ",bs)
print("traveling allowance",ta)
print("dearness allowance ",da)
print("House  rent allowance ",hra)
print("Gross salary ",gs)
print("Tax deducted source ",tds)
print("Net salary ",ns)
print("-----------------------------------------------------------------------------------------------------------------")
print("\t\t\tMonth :Dec 2024")
print("-----------------------------------------------------------------------------------------------------------------")
