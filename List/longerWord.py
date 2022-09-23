# Write a Python program to find the list of words that are longer than n from a given list of words.

list1=["aaa","aaaa",'aaaaa',"aaaaaa"]
list2=list1.copy()
length=4
for i in list2:
    if length>=len(i):
        list1.remove(i)

print(list1)