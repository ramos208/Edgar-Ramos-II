from tkinter import *
from tkinter import messagebox as proffMsg
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mongodb"]
mycol = mydb["customers"]

app = Tk()
app.title("Insert Application")
app.config(bg='lightpink')
width = 500
height = 300
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)
app.geometry('%dx%d+%d+%d' % (width, height, x, y))
app.resizable(0, 0)

# STRING VARIABLES
FIRSTNAME = StringVar()
LASTNAME = StringVar()
ADDRESS = StringVar()

# FRAME
lframe = LabelFrame(app, text="Registration Form", relief=SUNKEN, bg='lightblue', width='450', height='250')
lframe.pack()


def exit():
    msg = proffMsg.askquestion("Exit Application", "Do You Really Want To Quit Application", icon='info')
    if (msg == 'yes'):
        app.destroy()


def reg():
    if (FIRSTNAME.get() == "" or LASTNAME.get() == "" or ADDRESS.get() == ""):
        proffMsg.showinfo("Empty Form", "You Have To Fill All Form", icon='info')
    else:
        insert = [{"fname": (str(FIRSTNAME.get())), "lname": (str(LASTNAME.get())), "address": (str(ADDRESS.get()))}]
        mycol.insert_many(insert)
        Lcomm.config(text='Data Successfully Inserted', fg='green', bg='lightblue')


# LABEL ENTRY AND COMMAND TOOL INSERTION
# FIRSTNAME
flabel = Label(lframe, text='FIRSTNAME', fg='white', bg='lightblue', font=('lucida handwrition', 12))
flabel.place(x=160, y=10)
fentry = Entry(lframe, textvariable=FIRSTNAME)
fentry.place(x=160, y=30)

# LASTNAME
slabel = Label(lframe, text='LASTNAME', fg='white', bg='lightblue', font=('lucida handwrition', 12))
slabel.place(x=160, y=55)
sentry = Entry(lframe, textvariable=LASTNAME)
sentry.place(x=160, y=75)

# ADDRESS
Ladd = Label(lframe, text='ADDRESS', fg='white', bg='lightblue', font=('lucida handwrition', 12))
Ladd.place(x=160, y=100)
Eadd = Entry(lframe, textvariable=ADDRESS)
Eadd.place(x=160, y=120)

# BUTTON SUBMIT
bsubmit = Button(lframe, text='REGISTER', bg='lightpink', command=reg)
bsubmit.place(x=190, y=160)

Lcomm = Label(lframe, font=('lucida handwrition', 12), bg='lightblue')
Lcomm.place(x=140, y=180)

app.protocol('WM_DELETE_WINDOW', exit)
app.mainloop()