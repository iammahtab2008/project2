from tkinter import *
from tkinter import messagebox
import databasefile
win = Tk()
win.geometry('660x450')
win.configure(bg='#ffeee6')
db = databasefile.Database('e:/project2/database.db')
list_=[]
#=======func===========
def insert():
    fname = ent_fname.get()
    lname = ent_lname.get()
    course = ent_course.get()
    password = ent_password.get()
    if fname == '' or lname == '' or course == '' or password == '':
        messagebox.showerror('eror','You have to input data!!!')
        return
    else: 
        db.insert(fname, lname, course, password)
        messagebox.showinfo('success','user added successfuly!!!')
        clear() 


def see_all():
    datas = db.get_all_users()
    lst.delete(0,END)
    for data in datas:
        lst.insert(END,f'{data[0]},{data[1]},{data[2]},{data[3]},{data[4]}') 
        #I shouldn't get the password but anyways!!
    
def clear():
    ent_fname.delete(0,END)
    ent_lname.delete(0,END)
    ent_course.delete(0,END)
    ent_password.delete(0,END)
    ent_fname.focus_set()

def show(event):
    global list_
    index = lst.curselection()
    data = lst.get(index)
    list_ = data.split(',')
    clear()
    ent_fname.insert(END,list_[1])
    ent_lname.insert(END,list_[2])
    ent_course.insert(END,list_[3])
    ent_password.insert(END,list_[4])

def delete():
    global list_
    yesno = messagebox.askquestion('are u sure?','are u sure?')
    if yesno == 'yes':
        db.delete_user(list_[0])
        messagebox.showinfo('success','user deleted successfuly!!!') 
        clear()
        lst.delete(0,END)
    else:
        return

def exit():
    yesno = messagebox.askquestion('are u sure?','are u sure?')
    if yesno == 'yes':
        win.destroy()

def login():
    enter_password = ent_enter_password.get()
    passwords = db.get_all_passwords()
    if ent_password not in passwords:
        messagebox.showerror('eror','password not found!!')
        return
    user_login = db.find_user_by_password(enter_password)
    messagebox.showinfo('welcome',f'{user_login[0]} {user_login[1]},welcome')

#=======widget===========
'''label'''
lbl_fname = Label(win,text='fname',font='cambria 16 bold',bg='#ffeee6')
lbl_fname.grid(row=0,column=0,padx=10,pady=10)

lbl_lname = Label(win,text='lname',font='cambria 16 bold',bg='#ffeee6')
lbl_lname.grid(row=0,column=3,padx=10,pady=10)

lbl_course = Label(win,text='course',font='cambria 16 bold',bg='#ffeee6')
lbl_course.grid(row=1,column=0,padx=10,pady=10)

lbl_password = Label(win,text='password',font='cambria 16 bold',bg='#ffeee6')
lbl_password.grid(row=1,column=3,padx=10,pady=10)

lbl_enter_password = Label(win,text='enter password:',font='cambria 16 bold',bg='#ffeee6')
lbl_enter_password.place(x=30,y=385)

'''entry'''
ent_fname = Entry(win,font='cambria 14 bold',bg='#ffccff',width=16)
ent_fname.grid(row=0,column=2,padx=2,pady=10)

ent_lname = Entry(win,font='cambria 14 bold',bg='#ffccff',width=16)
ent_lname.grid(row=0,column=4,padx=2,pady=10)

ent_course = Entry(win,font='cambria 14 bold',bg='#ffccff',width=16)
ent_course.grid(row=1,column=2,padx=2,pady=10)

ent_password = Entry(win,font='cambria 14 bold',bg='#ffccff',width=16)
ent_password.grid(row=1,column=4,padx=2,pady=10)

ent_enter_password = Entry(win,font='cambria 15 bold',bg='#ffccff',width=22)
ent_enter_password.place(x=200,y=390)

'''button'''
btn_see_all =Button(win,text='See all',font='cambria 14 bold',bg='#ffccff',width=11,command=see_all)
btn_see_all.place(x=500,y=110)

btn_insert =Button(win,text='insert',font='cambria 14 bold',bg='#ffccff',width=11,command=insert)
btn_insert.place(x=500,y=160)

btn_clear =Button(win,text='clear',font='cambria 14 bold',bg='#ffccff',width=11,command=clear)
btn_clear.place(x=500,y=210)

btn_delete =Button(win,text='delete',font='cambria 14 bold',bg='#ffccff',width=11,command=delete)
btn_delete.place(x=500,y=260)

btn_exit =Button(win,text='exit',font='cambria 14 bold',bg='#ffccff',width=11,command=exit)
btn_exit.place(x=500,y=310)

btn_login =Button(win,text='login',font='cambria 14 bold',bg='#ffccff',width=11,command=login)
btn_login.place(x=500,y=360)

'''listbox'''
lst = Listbox(win,font='cambria 14 bold',bg='#ffccff',width=40,height=11)
lst.place(x=25,y=120)
lst.bind('<<ListboxSelect>>',show)

win.mainloop()