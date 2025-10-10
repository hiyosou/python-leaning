import shutil

with open('./data/source.txt','w') as file:
    file.write("katoujunitisaikyo")
shutil.copy('./data/source.txt','./data/copy_sorce.txt')
print("コピーしました")