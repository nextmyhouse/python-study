import os
location = "C:\\Users\\jbc\\Desktop\\jbc\\test"
file_name = os.listdir(location)
dic = {'FILE':{'py':[],'txt':[],'png':[],'etc':[]}}
for file_type in file_name:
    if file_type.endswith(".py"):
        dic['FILE']['py'].append(file_type)
    if file_type.endswith(".txt"):
        dic['FILE']['txt'].append(file_type)
    if file_type.endswith(".png"):
        dic['FILE']['png'].append(file_type)
    if file_type.endswith(".etc"):
        dic['FILE']['etc'].append(file_type)
print dic["FILE"]
