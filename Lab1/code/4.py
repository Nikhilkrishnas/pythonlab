import copy
sentence= input("enter the string") # taking the string as input
substr=[]
substr2=[]
max=0
for i in range(len(sentence)):
    if sentence[i] not in substr: #searching if the letter is in the substring
        substr.append(sentence[i]) #adding the letter to substring
    else:
        if len(substr)>max: #if the length of substring is greater than the maximun length
            substr2.clear()
            substr2=copy.deepcopy(substr)
            substr.clear()
            substr.append(sentence[i])
            max=len(substr2)
        else:
            substr.clear()
if len(substr)>max:
    substr2.clear()
    substr2 = copy.deepcopy(substr)
    max=len(substr2)
print(substr2," ",max)

