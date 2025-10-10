import os
file=open('./data/sample.txt','w')
file.write('Hello,World!')
file.close()
with open('./data/sample.txt','r') as file:
    print(file.read())

file=os.remove("./data/sample.txt")
