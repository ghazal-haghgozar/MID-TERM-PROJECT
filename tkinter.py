# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 02:34:08 2022

@author: Hpp
"""

import tkinter
import json

def submit_func():
    lbl.configure(text='')
    user=ent1.get()
    password=ent2.get()
    with open("d:/info.json") as f:
        dct=json.load(f)
    if user in dct :
        lbl.configure(text="username already exist")
    else:
        dct[user]=password
        with open('d:/info.json','w') as f:
            json.dump(dct,f)
        lbl.configure(text='account created successfully')
def login_func():
    lbl.configure(text='')
    user=ent1.get()
    password=ent2.get()
    with open("d:/info.json") as f:
        dct=json.load(f)
    if user in dct and dct[user]==password:
        lbl.configure(text='welcome')
    else:
        lbl.configure(text='account does not exist')
def del_func():
    lbl.configure(text='')
    user=ent1.get()
    password=ent2.get()
    with open("d:/info.json") as f:
        dct=json.load(f)
    if user in dct and dct[user]==password:
        dct.pop(user)
        with open('d:/info.json','w') as f:
            json.dump(dct,f)
        lbl.configure(text='account deleted')
    else:
        lbl.configure(text='username not found')
    
tab=tkinter.Tk()
tab.title("new tab")
tab.geometry("350x300")
lbl=tkinter.Label(text='')
lbl.grid(column=1,row=3)
lbl1=tkinter.Label(tab,text='username',font='arial')
lbl1.grid(column=0,row=0)
lbl2=tkinter.Label(tab,text='password',font='arial')
lbl2.grid(column=0,row=2)
ent1=tkinter.Entry(width=30)
ent1.grid(column=1,row=0)
ent2=tkinter.Entry(width=30)
ent2.grid(column=1,row=2)
btn1=tkinter.Button(text='submit',command=submit_func,width=10)
btn1.grid(column=0,row=4)
btn2=tkinter.Button(text='login',command=login_func,width=10)
btn2.grid(column=1,row=4)
btn3=tkinter.Button(text='delete',command=del_func,width=10)
btn3.grid(column=2,row=4)

tab.mainloop()
