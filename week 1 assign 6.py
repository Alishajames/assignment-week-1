sentence="""my name is alisha, and her name is tina"""
text=sentence
x=text.split()
print(x)
dict={}
for i in x:
    if i in dict.keys():
        dict[i]=dict[i]+1
    else:
        dict[i]=1
print(dict)



