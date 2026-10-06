#1. file read
#2. File write
#3. File append
#4. File search
#5. File remove
#6. Exit
from logging import config


def file_read():
    file_name=input('enter the file name')
    f=open(file_name,'r')
    content=f.read()
    print(content)

def file_write():
    file_name=input('enter the file name')
    f=open(file_name,'w')
    content=input('enter the file content')
    f.write(content)

def file_append():
    file_name=input('enter the file name')
    f=open(file_name,'a')
    content=input('enter the file content')
    f.write(content)

def file_search():
    file_name=input('enter the file name')
    f=open(file_name,'r')
    content = f.read()
    search=input('enter the file content')
    if search in f.read():
        print('file found')
    else:
        print('file not found')

def file_remove():
    import os
    file_name=input('enter the file name')
    os.remove(file_name)
    print('file','file_name','is deleted')


while(1):
    print('1.File read')
    print('2.File write')
    print('3.File append')
    print('4.File search')
    print('5.File remove')


    ch=int(input('Enter your choice:'))
    if ch==1:
        file_read()
    elif ch==2:
        file_write()
    elif ch==3:
        file_append()
    elif ch==4:
        file_search()
    elif ch==5:
        file_remove()
    else:
        exit()
