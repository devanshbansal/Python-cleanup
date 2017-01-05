import os
import shutil
list=[]
destdir="C:\\Users\lenovo\\Desktop\\Clean"
os.makedirs(destdir)

list=os.listdir("c:\\Users\\lenovo\\Desktop}_
for x in list:
    print x
    if x==__file__:
       continue
    shutil.move(x,destdir)