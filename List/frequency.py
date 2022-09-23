def frequency(list1):
    dictionary={}
    for word in list1:
        count=dictionary.get(word)
        if count==None:
            dictionary[word]=1
        else:
            dictionary[word]=count+1
    print(dictionary)
list1=[10,10,10,10,20,20,20,20,40,40,50,50,30]
frequency(list1)
