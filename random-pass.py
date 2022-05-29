import random
#  *************************  import Functions **********************

    #names=["shubham","harshit","rohini","kunal"]
    #print(random.choice(names))
    #print(random.randint(1000,9999))
    #print(random.random())

uppper_char=["A","B","C","E","F"]
lower_char=["a","b","c","d","e"]
num=["1","2","3","4","5"]
special_char=["@","#","^","&"]

passw=random.choice(uppper_char)+random.choice(lower_char)+random.choice(num)+random.choice(special_char)+random.choice(uppper_char)+random.choice(lower_char)+random.choice(num)+random.choice(special_char)
print(passw)