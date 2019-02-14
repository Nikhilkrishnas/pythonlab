list=[]
tupdict={}
tup=()
tup1=()
listtup=()
list1=[]
num=int(input("enter number of tuples"))
for i in range(num):
    tup = ()
    tup1 = ()
    listtup = ()
    name=input("enter the name")
    temp=tuple([name])
    sub=input("enter subject name")
    temp1=tuple([sub])
    marks=input("enter marks for that subject")
    temp2=tuple([marks])
    tup1=temp1+temp2
    listtup=temp,tup1
    list.append(listtup)
    del tup
    del tup1
    del temp
    del temp1
    del temp2
    del listtup
for i in list:
    tup= i
    if tup[0] in tupdict:
        tup1= tup[1]+tupdict[tup[0]]
        tupdict[tup[0]]=tup1
    else:

        tupdict.update({tup[0]:tup[1]})
print(tupdict)