import os
total=0
path= input("enter file path") #take the file path as input
infile=open(path,'r')
line= infile.readline() #read the first line from the file
while line!="":       #loop runs until all the lines are read
    transaction= line.split(" ") #splitting the line into words and storing it as array
    if transaction[0].lower()== "deposit":  #if the input is deposit the the net amount is incremented by the particular amount
        total+=int(transaction[1])
    elif transaction[0].lower()=="withdraw": #if the input is deposit the the net amount is decremented by the particular amount
        total-=int(transaction[1])
    transaction.clear()
    line=infile.readline()
print("total amount is: ",total)