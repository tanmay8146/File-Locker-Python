import os
from cryptography.fernet import Fernet
import tkinter.messagebox as box

def files():
    files_list = []
    try:
        for file in os.listdir():
            if file == 'keylock' or file == 'main.py':
                continue
            else:
                if os.path.isfile(file):
                    files_list.append(file)
    except:
        box.showerror(title='Error', message='No files in current directory')
    return files_list

def key():
    with open('keylock', 'rb') as keyread:
        key = keyread.read()
    if key:
        return key
    else:
        key = Fernet.generate_key()
        with open('keylock', 'wb') as newkey:
            newkey.write(key)
        return key

def locker():
    dir_files= files()
    secret_key= key()

    for file in dir_files:
        with open(file, 'rb') as fileread:
            file_contents= fileread.read()
        encrypted_contents= Fernet(secret_key).encrypt(file_contents)
        with open(file, 'wb') as filewrite:
            filewrite.write(encrypted_contents)
    box.showinfo(title='TanmayXD', message='Files locked! Take good care of the key file or your will lose your files forever.')

def unlocker():
    locked_files= files()
    secret_key= key()

    for file in locked_files:
        with open(file, 'rb') as fileread:
            encrypted_contents= fileread.read()
        decrypted_contents= Fernet(secret_key).decrypt(encrypted_contents)
        with open(file, 'wb') as filewrite:
            filewrite.write(decrypted_contents)
        box.showinfo(title='TanmayXD', message='Files unlocked!')

if __name__ == '__main__':
    from tkinter import *
    root= Tk()
    root.title('Locker by TanmayXD')
    root.geometry('300x300')
    lockBtn= Button(text='Lock', command=locker)
    unlockBtn= Button(text='Unlock', command=unlocker)

    lockBtn.place(x= 90, y=170)
    unlockBtn.place(x= 170, y= 170)

    exitBtn= Button(text='Exit', command=exit)
    exitBtn.place(x=130, y=220)

    root.mainloop()
