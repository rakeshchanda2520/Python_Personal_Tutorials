# Python program to check whether a list contains a sublist

list1=[10,20,30,40,50]
l1=len(list1)
list2=[10,20,30]
l2=len(list2)
for i in list1:
    if i==list2[0]:
        for j in range(l2):
            list1[i+j]==list2[j]
        else:
            print("sublist")
    else:
        print("not")
