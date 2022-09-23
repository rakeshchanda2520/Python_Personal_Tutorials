# Write a Python function that takes two lists and returns True if they have at least one common membe

list1=[1,2,3,4,5]
list2=[0,9,6,8]
count=0
for i in list1:
    for j in list2:
        if i==j:
            count+=1

if count>0:
    print(True)
else:
    print(False)