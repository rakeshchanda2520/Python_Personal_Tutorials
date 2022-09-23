# Python program to flatten a shallow lis

list1=[[2,4,3],[1,5,6], [9], [7,9,0]]
final_list=[]
for i in list1:
    for j in i:
        final_list.append(j)

print(final_list)

