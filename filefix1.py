import os
#defined
location = os.path.dirname(_file_)
original_name =  "new.txt"
change_name = "JBC is sexy king.txt"
#open
with open(original_name, "w") as f:
    f.write("moai king")
#change
os.rename(original_name, change_name)
#check
print os.path.exists(change_name)
#delete
os.remove(change_name)
