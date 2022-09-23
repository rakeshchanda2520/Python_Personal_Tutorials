# Python program to print the numbers of a specified list after removing even numbers from it.

list1=[1,2,3,5,4,6,8,9]
list2=list1.copy()
for i in list2:
    if i%2==0:
        list1.remove(i)
print(list1)
