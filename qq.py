#this is a comment
from tkinter import *
from tkinter import messagebox
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox
com = []
pay = []
bill = []

cname = []
pname = []
bname = []

count  = 1
count1 = 1
count2 = 1

# =================== Windows =================

def Exit():
    screen1.destroy()
def Reset():
    Win_Prio2.delete(0,'end')
    Win_Prio1.delete(0,'end')
    Win_Prio3.delete(0,'end')
    Win_Name1.delete(0,'end')
    Win_Name2.delete(0,'end')
    Win_Name3.delete(0,'end')

def Win3Next():
    global count2   
    if count2 <len(bill):
        Win_Prio3.delete(0,'end')
        Win_Name3.delete(0,'end')
        Win_Prio3.insert(END,bill[count2])
        Win_Name3.insert(END,bname[count2])
        count2 += 1
    else:
        result = tkMessageBox.showwarning('', 'no transaction', icon="warning")    
def Win2Next():
    global count1
    if  count1 < len(pay):
        Win_Prio2.delete(0,'end')
        Win_Name2.delete(0,'end')
        Win_Prio2.insert(END,pay[count1])
        Win_Name2.insert(END,pname[count1])
        count1 += 1
    else:
        result = tkMessageBox.showwarning('', 'no transaction', icon="warning")

def Win1Next():
    #PrioNum
    global count
    if  count < len(com):
        Win_Prio1.delete(0,'end')
        Win_Name1.delete(0,'end')
        Win_Prio1.insert(END,com[count])
        Win_Name1.insert(END,cname[count])
        count += 1
    else:
        result = tkMessageBox.showwarning('', 'no transaction', icon="warning")

        
# ============ Transactions ===============
def cs():
    if Entry_name.get()== "":
        result = tkMessageBox.showwarning('', 'Please enter your name', icon="warning")    
    else:      
        global a
        a = 0
        PrioNum.delete(0,END)
        p = 'CPN-'+str(len(com)+1)
        PrioNum.insert(END,p)
        com.append(p)
        cname.append(name.get())
    
    
def Payment():
    if Entry_name.get()== "":
        result = tkMessageBox.showwarning('', 'Please enter your name', icon="warning")    
    else:    
        global a
        a = 1
        PrioNum.delete(0,END)
        p = 'PPN-'+str(len(pay)+1)
        PrioNum.insert(END,p)
        pay.append(p)
        pname.append(name.get())
    

def Billing():
    if Entry_name.get()== "":
        result = tkMessageBox.showwarning('', 'Please enter your name', icon="warning")    
    else:
        global a
        a = 2
        PrioNum.delete(0,END)
        p = 'B-'+str(len(bill)+1)
        PrioNum.insert(END,p)
        bill.append(p)
        bname.append(name.get())        

# =================== Priority Number  ==================    
def Process():   
    if Entry_name.get()== "":
        result = tkMessageBox.showwarning('', 'Please Choose Transaction', icon="warning")
    else:
        PrioNum.delete(0,'end')
        Entry_name.delete(0,'end')        
        if a == 0:
            if len(cname) == 1 :
                print(len(com))
                Win_Prio1.insert(END,com[0])
                Win_Name1.insert(END,cname[0])
                #wait1.insert(END,len(com)-1)
        elif a == 1:
            if len(pname) == 1:
                Win_Prio2.insert(END,pay[0])
                Win_Name2.insert(END,pname[0])
        elif a == 2:
            if len(bname) == 1:
                Win_Prio3.insert(END,bill[0])
                Win_Name3.insert(END,bname[0])          
        
       


# ===================== Main Window ===================
def main():
    global PrioNum
    global name
    global Entry_name
    global Win_Prio1
    global Win_Name1
    global Win_Prio2
    global Win_Name2
    global Win_Prio3
    global Win_Name3
    global screen1
    screen1 = Tk()
    windowWidth = 1000
    windowHeight = 510
    print(screen1.winfo_screenheight())
    print(screen1.winfo_screenwidth())
    print("test calculate the window :)\nge set up nga width og height","Width",windowWidth,"Height",windowHeight)
    positionRight = int(screen1.winfo_screenwidth()/2 - windowWidth/2)
    positionDown = int(screen1.winfo_screenheight()/2 - windowHeight/2)
    screen1.geometry("{}x{}+{}+{}".format(windowWidth,windowHeight,positionRight, positionDown))
    screen1.config(bg = 'light gray')
    screen1.resizable(width=False,height=False)
    # ================= Left window ========================
    f1 = Frame(bd = 5,relief = SUNKEN,height = 500,width  = 495,bg = 'red',highlightbackground="#8293ee", highlightcolor="#8293ee", highlightthickness=5)    
    # ====== Logo and name =======  
    pic1 = PhotoImage(file = 'pldt.png')
    logo = Label(f1,image = pic1,bg = 'red',height = 75,relief = RIDGE,width=250,bd=5)#.place(x = 1, y = 250)
    f1.place(x = 5,y  = 0)
    logo.place(x = 125,y = 0)
    Label(text = 'Name: ',font = ('Arial',15,'bold'),bg = 'red',fg="white").place(x = 25, y = 100)
    name = StringVar()
    Entry_name = Entry(width = 25,font = ('Arial',18,'bold'),bg = 'white',textvar = name,relief="sunken",bd=5)
    Entry_name.place(x = 100, y = 95)
    # ====== Transactions ========
    Label(f1,bg = 'red',fg = 'white',text = 'Choose transaction: ',font = ('Arial',15,'bold')).place(x = 115, y = 150)
    btn1 = Button(f1,bg = 'white',fg="red",relief= "raised",bd=8,text = 'Customer Service',font = ('Arial',15,'bold'),command = cs,width=15).place(x = 150, y = 190)
    btn2 = Button(f1,bg = 'white',fg="red",relief= "raised",bd=8,text = 'Payment',font = ('Arial',15,'bold'),command = Payment,width=15).place(x = 150, y = 250)
    btn3 = Button(f1,bg = 'white',fg="red",relief= "raised",bd=8,text = 'Billing',font = ('Arial',15,'bold'),command = Billing,width=15).place(x = 150, y = 310)
    # ====== Priority number ========
    f3 = Frame(bg = 'light gray',bd = 5,relief= "ridge",height = 110,width  = 450)
    #f3.place(x = 25, y = 360)
    Label(text = 'Priority number: ',font = ('Arial',15,'bold'),fg="red",bg="white").place(x = 30, y = 380)
    f3.place(x = 25, y = 380)
    PrioNum = Entry(bd = 5,fg = 'red',relief = "sunken",width = 19,font = ('Arial',22,'bold'),bg = 'white')
    PrioNum.place(x = 35, y = 415)
    btn4 = Button(text = 'Confirm',font = ('Arial',15,'bold'),command = Process,bg = 'white',fg="red",relief="raised",bd=5).place(x = 360, y = 415)
    # ================= Right window ========================
    f2 = Frame(bd=5,bg = 'red',highlightbackground="#8293ee", highlightcolor="#8293ee", highlightthickness=5,height = 500,width  = 500,relief="sunken")
    f2.place(x = 490, y = 0)
    # ======== Windows ============
    Win1 = Frame(bg = 'light gray',bd = 5,relief = "ridge",height = 90,width  = 460)
    Win1.place(x = 510, y = 35)
    Label(text = 'Window 1',font = ('Arial',12,'bold'),bg = 'red',fg="white").place(x = 880, y = 25)
    Label(text = 'Now Serving: ',font = ('Arial',12,'bold'),bg = 'white',fg = 'red').place(x = 520, y = 40)
    Win_Prio1 = Entry(bd = 1,fg = 'red',relief = SOLID,width = 8,font = ('Arial',22,'bold'))
    Win_Prio1.place(x = 522, y = 70)
    Win_Name1 = Entry(bd = 1,fg = 'red',relief = FLAT,width = 18,font = ('Arial',20,'bold'))
    Win_Name1.place(x = 660, y = 60)
    Win2 = Frame(bg = 'light gray',bd = 5,relief = "ridge",height = 90,width  = 460)
    Win2.place(x = 510, y = 155)
    Label(text = 'Window 2 ',font = ('Arial',12,'bold'),bg = 'red',fg="white").place(x = 880, y = 145)    
    Label(text = 'Now Serving: ',font = ('Arial',12,'bold'),bg = 'white',fg = 'red').place(x = 520, y = 160)
    Win_Prio2 = Entry(bd = 1,fg = 'red',relief = SOLID,width = 8,font = ('Arial',22,'bold'))
    Win_Prio2.place(x = 522, y = 190)
    Win_Name2 = Entry(bd = 1,fg = 'red',relief = FLAT,width = 18,font = ('Arial',20,'bold'))
    Win_Name2.place(x = 660, y = 180)
    Win3 = Frame(bg = 'light gray',bd = 5,relief = "ridge",height = 90,width  = 460)
    Win3.place(x = 510, y = 275)
    Label(text = 'Window 3 ',font = ('Arial',12,'bold'),bg = 'red',fg="white").place(x = 880, y = 265) 
    Label(text = 'Now Serving: ',font = ('Arial',12,'bold'),bg = 'white',fg = 'red').place(x = 520, y =285)
    Win_Prio3 = Entry(bd = 1,fg = 'red',relief = SOLID,width = 8,font = ('Arial',22,'bold'))
    Win_Prio3.place(x = 522, y = 315)
    Win_Name3 = Entry(bd = 1,fg = 'red',relief = FLAT,width = 18,font = ('Arial',20,'bold'))
    Win_Name3.place(x = 660, y = 300)
    Win3 = Frame(bg = 'light gray',bd = 5,relief = "ridge",height = 90,width  = 460)
    Win3.place(x = 510, y = 390)
    Label(text = 'Window 1: ',font = ('Arial',12,'bold'),bg = 'red',fg="white",relief=RIDGE,bd=2).place(x = 510, y = 380)
    Label(text = 'Window 2: ',font = ('Arial',12,'bold'),bg = 'red',fg="white",relief=RIDGE,bd=2).place(x = 600, y = 380)
    Label(text = 'Window 3: ',font = ('Arial',12,'bold'),bg = 'red',fg="white",relief=RIDGE,bd=2).place(x = 690, y = 380)
    n1 = Button(bg = 'white',fg="red",relief="raised",bd=4,text = 'Next',font = ('Arial',15,'bold'),command = Win1Next ).place(x = 520, y = 420)
    n2 = Button(bg = 'white',fg="red",relief="raised",bd=4,text = 'Next',font = ('Arial',15,'bold'),command = Win2Next).place(x = 610, y = 420)
    n3 = Button(bg = 'white',fg="red",relief="raised",bd=4,text = 'Next',font = ('Arial',15,'bold'),command = Win3Next).place(x = 700, y = 420)
    close = Button(bg = '#530023',fg="white",text = 'Exit',font = ('Arial',15,'bold'),command = Exit,justify="center",bd=5,relief="raised").place(x = 880, y = 420)
    reset = Button(bg = '#530023',fg="white",text = 'Reset',font = ('Arial',15,'bold'),command = Reset,justify="center",bd=5,relief="raised").place(x = 800, y = 420)
    screen1.mainloop()
main()
