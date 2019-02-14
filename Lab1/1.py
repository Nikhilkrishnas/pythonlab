import os
total=0
path= input("enter file path")
infile=open(path,'r')
line= infile.readline()
while line!="":
    transaction= line.split(" ")
    if transaction[0].lower()== "deposit":
        total+=int(transaction[1])
    elif transaction[0].lower()=="withdraw":
        total-=int(transaction[1])
    transaction.clear()
    line=infile.readline()
print("total amount is: ",total)